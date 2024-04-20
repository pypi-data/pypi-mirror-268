from abc import ABC, abstractmethod
from typing import Optional

import httpx
from asynctaskpool import AsyncTaskPool
from httpx import Cookies, Response

from .request_exceptions import UnauthenticatedError

_authentication_task_id = "authentication"


class GenericAuthenticator(ABC):
    max_retries = 3

    def __init__(self, client: httpx.AsyncClient):
        self._client = client
        # This task pool only ever has 1 specific task submitted to it - the authentication task.
        self._authentication_singleton_taskpool = AsyncTaskPool(restart_if_finished=True)

    async def do_request_and_authenticate_if_necessary(self, request: httpx.Request, stream: bool = False,
                                                       follow_redirects: Optional[bool] = None):
        await self._wait_for_authentication_task_to_finish()

        self._update_request_cookies(request)

        options = dict(stream=stream, follow_redirects=follow_redirects or self._client.follow_redirects)
        response = await self._client.send(request, **options)
        retry_count = 0

        while self._detect_if_authentication_is_needed(response) and self._should_keep_retrying(retry_count):
            retry_count += 1

            await self._run_authentication_or_wait_for_it_to_finish_if_already_running()
            self._update_request_cookies(request)
            response = await self._client.send(request, **options)

        if not self._should_keep_retrying(retry_count) and self._detect_if_authentication_is_needed(response):
            raise UnauthenticatedError(f"Could not authenticate the client in under {self.max_retries} tries")

        return response

    async def _wait_for_authentication_task_to_finish(self):
        await self._authentication_singleton_taskpool.wait_for_task_to_finish_if_running(_authentication_task_id)

    def _update_request_cookies(self, request):
        Cookies(self._client.cookies).set_cookie_header(request)

    def _should_keep_retrying(self, retry_count: int) -> bool:
        return retry_count < self.max_retries

    async def _run_authentication_or_wait_for_it_to_finish_if_already_running(self):
        await self._authentication_singleton_taskpool.submit_new_task(_authentication_task_id, self._authenticate())

    @abstractmethod
    def _detect_if_authentication_is_needed(self, response: Response) -> bool:
        ...

    @abstractmethod
    async def _authenticate(self):
        ...
