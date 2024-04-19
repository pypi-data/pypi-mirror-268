from httpx import Response

from qcanvas_api_clients.canvas.canvas_client import CanvasClient
from qcanvas_api_clients.panopto.panopto_api_config import PanoptoApiConfig
from qcanvas_api_clients.util.generic_authenticator import GenericAuthenticator


class PanoptoAuthenticator(GenericAuthenticator):
    def __init__(self, panopto_api_config: PanoptoApiConfig, canvas_client: CanvasClient):
        super().__init__(canvas_client.client)
        self._panopto_api_config = panopto_api_config
        self._canvas_client = canvas_client

    def _detect_if_authentication_is_needed(self, response: Response) -> bool:
        auth_cookie = ".ASPXAUTH"
        return auth_cookie not in response.cookies.keys() or response.cookies.get(auth_cookie) == ""

    async def _authenticate(self):
        await self._canvas_client.authenticate_to_panopto(self._panopto_api_config.get_endpoint("/Panopto/Pages/Auth/Login.aspx?instance=Canvas&AllowBounce=true"))





