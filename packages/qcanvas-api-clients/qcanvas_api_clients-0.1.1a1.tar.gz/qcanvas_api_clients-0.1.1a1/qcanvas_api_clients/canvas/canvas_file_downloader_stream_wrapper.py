from httpx import Request, Response

from qcanvas_api_clients.canvas.canvas_authenticator import CanvasAuthenticator


class CanvasFileDownloaderStreamWrapper:
    def __init__(self, request: Request, authentication_manager: CanvasAuthenticator):
        self._authentication_manager = authentication_manager
        self._request = request

    async def __aenter__(self) -> Response:
        self.stream = await self._authentication_manager.do_request_and_authenticate_if_necessary(
            self._request,
            stream=True,
            follow_redirects=True
        )

        return self.stream

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stream.aclose()
