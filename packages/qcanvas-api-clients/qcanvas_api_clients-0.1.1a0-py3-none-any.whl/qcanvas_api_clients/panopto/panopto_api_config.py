from httpx import URL

from qcanvas_api_clients.util.url_converter import ensure_is_url


class PanoptoApiConfig:
    def __init__(self, panopto_url: str | URL):
        self._panopto_url = ensure_is_url(panopto_url)

    def get_endpoint(self, path: URL | str):
        return self._panopto_url.join(path)
