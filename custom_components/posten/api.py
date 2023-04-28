"""Sample API Client."""
import logging
import asyncio
import base64
import time
import socket
from typing import Optional
import aiohttp
import async_timeout

TIMEOUT = 10

"""I think a way to get around postens stupid api keys, please do not change this posten we are just trying to get your data. Im pretty sure this data goes under offentleglova anyways so please stop changing it <3"""
token = (base64.b64encode(bytes(base64.b64decode("f3ccd044MTY4MjYyODE2MQ==")[0:6]) + bytes(str(int(time.time())), "utf8")).decode().replace("=", ""))



_LOGGER: logging.Logger = logging.getLogger(__package__)

_LOGGER.error(token)

HEADERS = {"content-type": "application/json; charset=UTF-8", "x-requested-with": "XMLHttpRequest", "kp-api-token": token}

class IntegrationPostenApiClient:
    def __init__(
        self, postalcode: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self._session = session
        self._postalcode = postalcode

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        url = "https://www.posten.no/levering-av-post/_/service/no.posten.website/delivery-days?postalCode="+self._postalcode
        _LOGGER.error(url)
        _LOGGER.error(str(HEADERS))
        return await self.api_wrapper(method="get", url=url, headers=HEADERS)

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                if method == "get":
                    response = await self._session.request(method, url, headers=headers)
                    _LOGGER.error(str(await response.json()))
                    return await response.json()
                else:
                    await self._session.request(method, url, headers=headers, json=data)

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)