from typing import List

from aiohttp import ClientSession

from .cmi_api import CMIAPI
from .const import ReadOnlyClass
from .device import Device


class CMI(metaclass=ReadOnlyClass):
    """Main class to interact with CMI."""

    def __init__(
        self, host: str, username: str, password: str, session: ClientSession = None
    ) -> None:
        """Initialize."""
        self._api = CMIAPI(host, username, password, session)

    async def get_devices(self) -> List[Device]:
        """List connected devices."""
        device_ids = await self._api.get_devices_ids()

        return [Device(x, self._api) for x in device_ids]
