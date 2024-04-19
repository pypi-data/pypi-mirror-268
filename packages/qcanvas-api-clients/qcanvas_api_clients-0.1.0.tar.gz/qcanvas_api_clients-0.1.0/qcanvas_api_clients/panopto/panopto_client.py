import asyncio
import json
from typing import Optional

from httpx import Response, URL, Request

from qcanvas_api_clients.canvas.canvas_client import CanvasClient
from qcanvas_api_clients.panopto.panopto_api_config import PanoptoApiConfig
from qcanvas_api_clients.panopto.panopto_authenticator import PanoptoAuthenticator
from tenacity import retry, wait_exponential, wait_random, stop_after_attempt, retry_if_exception_type

from qcanvas_api_clients.util.request_exceptions import RatelimitedError

# todo unfinished

class PanoptoClient:
    def __init__(self, panopto_api_config: PanoptoApiConfig, canvas_client: CanvasClient,
                 max_concurrent_operations: int = 20):
        self._api_config = panopto_api_config
        self._canvas_client = canvas_client
        self._authentication_controller = PanoptoAuthenticator(self._api_config, self._canvas_client)
        self._concurrent_request_limiter = asyncio.Semaphore(max_concurrent_operations)

    # async def get_folders(self) -> ListResponseOfFolder:
    #     response = (await self._execute_request(
    #         method="POST",
    #         endpoint_path=f"/api/v1/folders/",
    #         content="""{"queryParameters":{}}"""
    #     ))
    #
    #     with open("result.json", "w") as o:
    #         o.write(response.text)
    #
    #     result_json = json.loads(response.text)
    #     return ListResponseOfFolder(**result_json)

    @retry(
        wait=wait_exponential(exp_base=1.2, max=10) + wait_random(0, 1),
        retry=retry_if_exception_type(RatelimitedError),
        stop=stop_after_attempt(8)
    )
    async def _execute_request(self, endpoint_path: str | URL, method: str = "GET",
                               content: Optional[str] = None) -> Response:
        request = Request(
            method=method,
            url=self._api_config.get_endpoint(endpoint_path),
            content=content,
            headers={
                "accept": "application/json",
                "content-type": "application/json"
            }
        )

        async with self._concurrent_request_limiter:
            response = await self._authentication_controller.do_request_and_authenticate_if_necessary(request)

        if response.status_code == 429:
            raise RatelimitedError()

        return response
