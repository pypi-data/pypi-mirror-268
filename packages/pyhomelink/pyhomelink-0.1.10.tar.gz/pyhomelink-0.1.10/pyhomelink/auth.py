"""HomeLINK Auth."""
import json
import logging
import os
from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional

from aiohttp import ClientError, ClientResponse, ClientSession

from .const import BASE_URL

AUTHURL = "https://auth.live.homelync.io/oauth2"
AUTHORIZATION_HEADER = "Authorization"

_LOGGER = logging.getLogger(__name__)


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(
        self,
        websession: ClientSession,
    ):
        """Initialize the auth."""
        self._websession = websession
        self._base_url = self._get_base_url()

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(
        self, method: str, url_suffix: str, **kwargs: Optional[Mapping[str, Any]]
    ) -> ClientResponse:
        """Make a request."""
        try:
            access_token = await self.async_get_access_token()
        except ClientError as err:
            raise RuntimeError(f"Access token failure: {err}") from err
        headers = {
            AUTHORIZATION_HEADER: f"Bearer {access_token}",
            "accept": "application/json",
            "user-agent": "pyhomelink",
        }
        if self._base_url != BASE_URL:
            headers["x-mock-response-name"] = self._get_x_mock_response_name(url_suffix)
            _LOGGER.debug("headers %s", headers["x-mock-response-name"])

        url = f"{self._base_url}{url_suffix}"
        _LOGGER.debug("request[%s]=%s %s", method, url, kwargs.get("params"))
        if method == "post" and "json" in kwargs:
            _LOGGER.debug("request[post json]=%s", kwargs["json"])
        return await self._websession.request(method, url, **kwargs, headers=headers)

    async def async_get_token(
        self, url: str, **kwargs: Optional[Mapping[str, Any]]
    ) -> ClientResponse:
        """Make a request."""
        url = f"{AUTHURL}{url}"
        _LOGGER.debug(
            "request[%s]=%s %s", "get", "Auth get token", kwargs.get("params")
        )
        return await self._websession.request("get", url, **kwargs)

    def _get_base_url(self):
        base_url = BASE_URL
        json_path = self._dev_file_name()
        if os.path.isfile(json_path):
            with open(json_path, "r", encoding="UTF8") as infile:
                file_content = json.load(infile)

            return file_content["dev_url"]

        return base_url

    def _get_x_mock_response_name(self, url_suffix):
        json_path = self._dev_file_name()
        with open(json_path, "r", encoding="UTF8") as infile:
            file_content = json.load(infile)

        return file_content["x-mock-response-name"][url_suffix]

    def _dev_file_name(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return f"{dir_path}/../test_data/homelink_test.json"
