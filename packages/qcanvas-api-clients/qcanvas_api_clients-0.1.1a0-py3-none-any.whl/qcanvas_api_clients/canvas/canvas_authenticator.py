import json

import httpx
from httpx import Response

from qcanvas_api_clients.canvas.canvas_api_config import CanvasApiConfig
from qcanvas_api_clients.util.generic_authenticator import GenericAuthenticator
from qcanvas_api_clients.util.request_exceptions import AuthenticationFailedError


class CanvasAuthenticator(GenericAuthenticator):
    def __init__(self, client: httpx.AsyncClient, canvas_api_config: CanvasApiConfig):
        super().__init__(client)
        self._canvas_api_config = canvas_api_config

    def _detect_if_authentication_is_needed(self, response: Response) -> bool:
        # Canvas will silently redirect to the login page or give a 401 if we are not authenticated
        return response.url.path == "/login/canvas" or response.status_code == 401

    async def _authenticate(self):
        legacy_authentication_url = await self.request_legacy_authentication_url()
        response = await self._client.get(legacy_authentication_url)

        if not response.is_redirect:
            raise AuthenticationFailedError("Authentication was not successful")

    async def request_legacy_authentication_url(self) -> str:
        response = await self._client.get(
            url=self._canvas_api_config.get_endpoint("/login/session_token"),
            headers=self._canvas_api_config.get_authorization_header()
        )

        if response.is_success:
            return self._get_legacy_authentication_url_from_response(response)
        else:
            raise AuthenticationFailedError("Authentication failed, check your API key")

    @staticmethod
    def _get_legacy_authentication_url_from_response(session_response) -> str:
        target_url = json.loads(session_response.text)["session_url"]

        if target_url is None:
            raise AuthenticationFailedError("Session response body was malformed")
        else:
            return target_url
