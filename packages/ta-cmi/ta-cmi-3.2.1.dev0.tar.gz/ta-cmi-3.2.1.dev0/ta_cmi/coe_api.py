from typing import Any, Dict

from aiohttp import ClientSession

from .api import API
from .coe_channel import CoEChannel
from .const import _LOGGER, ChannelMode


class CoEAPI(API):
    """Class to perform API requests to the CoE Addon."""

    COE_VERSION = "/version"
    COE_DATA = "/receive/{id}"
    COE_SEND_ANALOG = "/send/analog"
    COE_SEND_DIGITAL = "/send/digital"

    DIGITAL_VALUES_PER_PAGE = 16
    ANALOG_VALUES_PER_PAGE = 4

    def __init__(self, host: str, session: ClientSession = None) -> None:
        """Initialize."""
        super().__init__(session)

        self.host = host

    async def get_coe_data(self, can_id: int) -> Dict[str, Any] | None:
        """Get the CoE data."""
        url = f"{self.host}{self.COE_DATA.replace('{id}', str(can_id))}"

        _LOGGER.debug("Receive data from CoE server: %s", url)

        data = await self._make_request_get(url)

        _LOGGER.debug("Received data from CoE server: %s", data)

        if len(data) == 0:
            return None

        return data

    async def get_coe_version(self) -> str | None:
        """Get the version of the CoE server."""
        url = f"{self.host}{self.COE_VERSION}"

        _LOGGER.debug("Receive current version from CoE server: %s", url)

        data = await self._make_request_get(url)

        _LOGGER.debug("Received version from CoE server: %s", data)

        if len(data) == 0:
            return None

        return data.get("version", None)

    @staticmethod
    def _check_channel_mode(
        target_mode: ChannelMode, channel_to_check: list[CoEChannel]
    ) -> bool:
        """Check if the channel type equals the target."""
        for channel in channel_to_check:
            if channel.mode != target_mode:
                _LOGGER.warning(
                    f"Channel has wrong mode. Expected mode: {target_mode}, actual mode: {channel.mode}"
                )
                return False

        return True

    @staticmethod
    def _check_array_length(array: list, target_size: int) -> bool:
        """Check if a list has the required length."""
        if len(array) != target_size:
            _LOGGER.warning(
                f"List has wrong length. Expected length: {target_size}, actual length: {len(array)}"
            )
            return False

        return True

    @staticmethod
    def _check_analog_page_size(provided: int) -> bool:
        """Check if the page is in the right number range."""
        if not (0 < provided < 9):
            _LOGGER.warning(
                f"Page is not in the expected range. Expected range: 0 < page < 9, actual value: {provided}"
            )
            return False

        return True

    @staticmethod
    def _convert_analog_channel_to_dict(channel: CoEChannel) -> dict[str, Any]:
        """Convert a analog coe channel to a dict."""
        return {"value": channel.value, "unit": int(channel.unit)}

    async def send_analog_values(self, channels: list[CoEChannel], page: int):
        """Send analog values to the CoE server."""
        _LOGGER.debug("Send analog values to CoE server")

        if (
            not self._check_channel_mode(ChannelMode.ANALOG, channels)
            or not self._check_array_length(channels, self.ANALOG_VALUES_PER_PAGE)
            or not self._check_analog_page_size(page)
        ):
            _LOGGER.error("Could not send analog values. Please see logs for details.")
            return

        data = {
            "values": [
                self._convert_analog_channel_to_dict(channel) for channel in channels
            ],
            "page": page,
        }

        url = f"{self.host}{self.COE_SEND_ANALOG}"

        await self._make_request_post(url, data)

    async def send_digital_values(
        self, channels: list[CoEChannel], second_page: bool = False
    ) -> None:
        """Send digital values to the CoE server."""
        _LOGGER.debug("Send digital values to CoE server")

        if not self._check_channel_mode(
            ChannelMode.DIGITAL, channels
        ) or not self._check_array_length(channels, self.DIGITAL_VALUES_PER_PAGE):
            _LOGGER.error("Could not send digital values. Please see logs for details.")
            return

        data = {"values": [bool(x.value) for x in channels], "page": int(second_page)}

        url = f"{self.host}{self.COE_SEND_DIGITAL}"
        await self._make_request_post(url, data)
