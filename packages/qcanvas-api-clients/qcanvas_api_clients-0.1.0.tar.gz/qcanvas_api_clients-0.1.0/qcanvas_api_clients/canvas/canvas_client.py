import asyncio
import json
from typing import Any, Optional

import gql
from gql.client import DocumentNode as GraphQLQuery
import httpx
from httpx import Response, URL, Request
from tenacity import retry, wait_exponential, wait_random, stop_after_attempt, retry_if_exception_type

from qcanvas_api_clients.canvas.canvas_api_config import CanvasApiConfig
from qcanvas_api_clients.canvas.canvas_authenticator import CanvasAuthenticator
from qcanvas_api_clients.canvas.canvas_file_downloader_stream_wrapper import CanvasFileDownloaderStreamWrapper
from qcanvas_api_clients.canvas.legacy_canvas_types import LegacyPage, LegacyFile
from qcanvas_api_clients.util.request_exceptions import RatelimitedError
from qcanvas_api_clients.util.custom_httpx_async_transport import CustomHTTPXAsyncTransport


class CanvasClient:
    def __init__(self, api_config: CanvasApiConfig, max_concurrent_operations: int = 20, gql_timeout: int = 120):
        self._api_config = api_config
        self.client = httpx.AsyncClient()
        self._authentication_controller = CanvasAuthenticator(self.client, self._api_config)
        self._concurrent_request_limiter = asyncio.Semaphore(max_concurrent_operations)
        self._gql_timeout = gql_timeout

    async def run_graphql_query(self, query: GraphQLQuery, query_variables: dict[str, Any] = None) -> dict[str, Any]:
        if query_variables is None:
            query_variables = {}

        async with self._concurrent_request_limiter:
            gql_client = self._setup_graphql_client()

            return await gql_client.execute_async(
                document=query,
                variable_values=query_variables
            )

    def _setup_graphql_client(self) -> gql.Client:
        transport = CustomHTTPXAsyncTransport(
            client=self.client,
            url=self._api_config.get_endpoint("api/graphql"),
            headers=self._api_config.get_authorization_header()
        )

        return gql.Client(
            transport=transport,
            execute_timeout=120
        )

    def open_stream_to_download_file(self, file_url: str | URL) -> CanvasFileDownloaderStreamWrapper:
        return CanvasFileDownloaderStreamWrapper(
            request=self.client.build_request(
                method="GET",
                url=file_url
            ),
            authentication_manager=self._authentication_controller
        )

    async def get_temporary_session_link_for_quick_authentication(self) -> str:
        return await self._authentication_controller.request_legacy_authentication_url()

    async def get_page(self, page_id: str | int, course_id: str | int) -> LegacyPage:
        response = await self._execute_request(f"api/v1{course_id}/pages/{page_id}")
        response.raise_for_status()
        return LegacyPage.from_dict(json.loads(response.text))

    async def get_file(self, file_id: str | int, course_id: str | int) -> LegacyFile:
        response = await self._execute_request(f"api/v1/courses/{course_id}/files/{file_id}")
        response.raise_for_status()
        return LegacyFile.from_dict(json.loads(response.text))

    async def authenticate_to_panopto(self, authentication_url: str | URL) -> Response:
        request = Request(
            method="GET",
            url=authentication_url
        )

        return await self._execute_request_and_handle_retry_if_ratelimited(request, follow_redirects=True)

    async def _execute_request(self, endpoint_path: str | URL, method: str = "GET") -> Response:
        request = Request(
            method=method,
            url=self._api_config.get_endpoint(endpoint_path),
        )

        response = await self._execute_request_and_handle_retry_if_ratelimited(request)

        return response

    @retry(
        wait=wait_exponential(exp_base=1.2, max=10) + wait_random(0, 1),
        retry=retry_if_exception_type(RatelimitedError),
        stop=stop_after_attempt(8)
    )
    async def _execute_request_and_handle_retry_if_ratelimited(self, request: Request, follow_redirects: Optional[bool] = None) -> Response:
        async with self._concurrent_request_limiter:
            response = await self._authentication_controller.do_request_and_authenticate_if_necessary(request, follow_redirects=follow_redirects)

        self._detect_ratelimit_and_raise(response)

        return response


    @staticmethod
    def _detect_ratelimit_and_raise(response: Response):
        # Who the FUCK decided to use 403 instead of 429?? With this stupid message??
        # And the newline at the end for some fucking reason is the cherry on top...
        if response.status_code == 403 and response.text == "403 Forbidden (Rate Limit Exceeded)\n":
            raise RatelimitedError()
