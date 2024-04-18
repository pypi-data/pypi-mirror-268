import asyncio
from typing import List

from aiohttp import ClientSession

from .cmi_api import CMIAPI
from .const import SLEEP_FUNCTION_TYPE, ReadOnlyClass
from .device import Device


class CMI(metaclass=ReadOnlyClass):
    """Main class to interact with CMI."""

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        session: ClientSession = None,
        sleep_function: SLEEP_FUNCTION_TYPE = asyncio.sleep,
    ) -> None:
        """Initialize."""
        self._api = CMIAPI(host, username, password, session)
        self._sleep_function = sleep_function

    async def get_devices(self) -> List[Device]:
        """List connected devices."""
        device_ids = await self._api.get_devices_ids()

        return [
            Device(x, self._api, sleep_function=self._sleep_function)
            for x in device_ids
        ]
