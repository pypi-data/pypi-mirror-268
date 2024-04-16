import asyncio
from typing import Any, Dict, List

from .channel import Channel
from .cmi_api import CMIAPI
from .cmi_channel import CMIChannel
from .const import _LOGGER, DEVICES, SUPPORTED_PARAMS_FOR_DEVICE, ChannelType


class Device:
    """Class to interact with a device."""

    def __init__(self, node_id: str, api: CMIAPI) -> None:
        """Initialize."""
        super().__init__()

        self._channels: Dict[ChannelType, Dict[int, CMIChannel]] = {}

        self.id = node_id
        self._api = api

        self.api_version: int = 0
        self.device_id: str = "00"

    def _extract_device_info(self, json: Dict[str, Any]) -> None:
        """Extract device info from request response."""
        self.api_version: int = json["Header"]["Version"]
        self.device_id: str = json["Header"]["Device"]

        if self.device_id not in DEVICES.keys():
            raise InvalidDeviceError(f"Invalid device id: {self.device_id}")

    @staticmethod
    def _extract_channels(
        mode: ChannelType, raw_channels: List[Dict[str, Any]]
    ) -> Dict[int, CMIChannel]:
        """Extract channel info from data array from request."""
        list_of_channels: Dict[int, CMIChannel] = {}
        for channel_raw in raw_channels:
            ch: CMIChannel = CMIChannel(mode, channel_raw)
            list_of_channels[ch.index] = ch

        return list_of_channels

    def _get_json_params(self) -> str:
        """Compose json params based on the device type."""
        default_params = "I,O"
        return SUPPORTED_PARAMS_FOR_DEVICE.get(self.device_id, default_params)

    async def _make_request_to_device(self) -> Dict[str, Any]:
        """Make a request to the device."""
        params = self._get_json_params()
        return await self._api.get_device_data(self.id, params)

    async def fetch_type(self) -> None:
        """Fetch the device type without parsing the data from the device."""
        self._extract_device_info(await self._make_request_to_device())

    async def update(self) -> None:
        """Update data."""
        _LOGGER.debug("Update device: %s", self.id)
        res: Dict[str, Any] = await self._make_request_to_device()

        if self.device_id == "00":
            self._extract_device_info(res)
            _LOGGER.debug("Device had no id. Set new id to %s", self.device_id)

        for channel_type_text in res["Data"]:
            channel_type = ChannelType(channel_type_text)
            self._channels[channel_type] = self._extract_channels(
                channel_type, res["Data"][channel_type_text]
            )

    def set_device_type(self, device_name: str) -> None:
        """Set the type of the device manually."""
        type_id = [i for i in DEVICES if DEVICES[i] == device_name]

        if len(type_id) != 1:
            raise InvalidDeviceError(f"Invalid device name: {device_name}")

        self.device_id = type_id[0]

    def get_device_type(self) -> str:
        """Get the type of the device."""
        return DEVICES.get(self.device_id, "Unknown")

    def get_channels(self, channel_type: ChannelType) -> Dict[int, CMIChannel]:
        """Get all the fetched channels from a type."""
        return self._channels.get(channel_type, {})

    def has_channel_type(self, channel_type: ChannelType) -> bool:
        """Check if a channel type was fetched."""
        return self._channels.get(channel_type, None) is not None

    def __repr__(self) -> str:
        text = f"Node {self.id}: Type: {self.get_device_type()}"

        for channel_type in self._channels:
            text += f", {channel_type.value}: {len(self._channels[channel_type])}"

        return text


class InvalidDeviceError(Exception):
    """Triggered when an invalid device type is set."""

    def __init__(self, status: str) -> None:
        """Initialize."""
        super().__init__(status)
        self.status = status
