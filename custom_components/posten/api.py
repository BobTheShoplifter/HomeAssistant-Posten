"""Posten API Client."""
from __future__ import annotations

import asyncio
import base64
import socket
import time
from collections.abc import Mapping

import aiohttp

TIMEOUT = 10


class PostenApiError(Exception):
    """Posten API error."""


class IntegrationPostenApiClient:
    """Posten API Client."""

    def __init__(self, postalcode: str, session: aiohttp.ClientSession) -> None:
        """Psten API Client."""
        self._session = session
        self._postalcode = postalcode

    async def async_get_data(self) -> dict:
        """Get data from the API.

        I think a way to get around postens stupid api keys,
        please do not change this posten we are just trying to get your data.
        Im pretty sure this data goes under offentleglova anyways so please stop changing it <3
        """
        return await self.api_wrapper(
            method="get",
            url="https://www.posten.no/levering-av-post/_/service/no.posten.website/delivery-days",
            params={"postalCode": self._postalcode},
            headers={
                "content-type": "application/json; charset=UTF-8",
                "x-requested-with": "XMLHttpRequest",
                "kp-api-token": base64.b64encode(
                    bytes(base64.b64decode("f3ccd044MTY4MjYyODE2MQ==")[0:6])
                    + bytes(str(int(time.time())), "utf8")
                )
                .decode()
                .replace("=", ""),
            },
        )

    async def api_wrapper(
        self,
        method: str,
        url: str,
        headers: dict | None = None,
        params: Mapping[str, str] | None = None,
    ) -> dict:
        """Get information from the API."""
        try:
            async with self._session.request(
                method,
                url,
                headers=headers or {},
                params=params,
                timeout=aiohttp.ClientTimeout(total=TIMEOUT),
            ) as response:
                response.raise_for_status()
                data = await response.json()

        except asyncio.TimeoutError as exception:
            raise PostenApiError(
                f"Timeout error fetching information from {url}"
            ) from exception

        except (TypeError, ValueError) as exception:
            raise PostenApiError(
                f"Error parsing information from {url} - {exception}"
            ) from exception

        except (aiohttp.ClientError, socket.gaierror) as exception:
            raise PostenApiError(
                f"Error fetching information from {url} - {exception}"
            ) from exception

        if not isinstance(data, dict):
            raise PostenApiError(f"Invalid response from {url}: {data!r}")

        return data
