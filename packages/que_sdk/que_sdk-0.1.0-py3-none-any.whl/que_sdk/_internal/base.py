from collections.abc import (
    Mapping,
)
import logging
import ssl
from typing import (
    Any,
    Literal,
)

import backoff
import httpx

from que_sdk._internal.auth import (
    JWTAuth,
)

__all__ = ("BaseClient",)


class BaseClient:
    def __init__(self) -> None:
        self._base_url = "http://127.0.0.1:8080/api/v1"
        self.log = logging.getLogger(self.__class__.__name__)

    @backoff.on_exception(
        backoff.expo,
        httpx.ConnectError,
        max_time=60,
    )
    async def _make_request(
        self,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        url: str,
        access_token: str | None = None,
        params: Mapping[str, str] | None = None,
        headers: Mapping[str, str] | None = None,
        data: Mapping[str, str] | None = None,
        json: Mapping[str, str] | None = None,
    ) -> tuple[int, Any]:
        """Make request and return decoded json response"""
        ssl_context = ssl.SSLContext()
        transport = httpx.AsyncHTTPTransport(verify=ssl_context)
        if access_token:
            auth = JWTAuth(access_token)
        else:
            auth = None
        async with httpx.AsyncClient(
            base_url=self._base_url,
            transport=transport,
            auth=auth,
        ) as client:
            self.log.debug(
                "Making request %r %r with json %r and params %r",
                method,
                url,
                json,
                params,
            )
            response = await client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=headers,
                data=data,
                auth=auth,
            )
            status = response.status_code

            try:
                result = response.json()
            except Exception as ex:
                self.log.exception(ex)
                self.log.info(f"{response.text}")
                result = {}

            self.log.debug(
                "Got response %r %r with status %r and json %r",
                method,
                url,
                status,
                result,
            )

            return status, result
