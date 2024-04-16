import math
from unittest.mock import patch

import pytest

from ta_cmi import ChannelMode, ChannelType
from ta_cmi.coe import CoE
from ta_cmi.coe_channel import CoEChannel
from tests import (
    COE_DATA_PACKAGE,
    COE_SEND_ANALOG_PACKAGE,
    COE_SEND_DIGITAL_PACKAGE,
    COE_VERSION_CHECK_PACKAGE,
    COE_VERSION_PACKAGE,
)

TEST_HOST = "http://localhost"

DATA_RESPONSE = {
    "digital": [{"value": True, "unit": 43}],
    "analog": [{"value": 34.4, "unit": 1}],
    "last_update_unix": 1680410064.03764,
    "last_update": "2023-04-01T12:00:00",
}

DATA_RESPONSE_WITH_EMPTY_SLOTS = {
    "digital": [{"value": True, "unit": 43}, {"value": False, "unit": 0}],
    "analog": [
        {"value": 34.4, "unit": 1},
        {"value": 0.0, "unit": 0},
        {"value": 3.5, "unit": 0},
    ],
    "last_update_unix": 1680410064.03764,
    "last_update": "2023-04-01T12:00:00",
}


@pytest.mark.asyncio
async def test_update_no_data_received():
    """Test the update method with empty data."""
    coe = CoE(TEST_HOST)

    coe._channels = {}

    with patch(COE_DATA_PACKAGE, return_value=None) as data_mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.update(1)

        assert coe._channels == {}

        data_mock.assert_called_once()
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_update_old_data_received():
    """Test the update method with old data."""
    coe = CoE(TEST_HOST)

    can_id = 42

    coe._channels[can_id] = {ChannelType.INPUT: {}}
    coe.last_update[can_id] = DATA_RESPONSE["last_update_unix"]

    with patch(COE_DATA_PACKAGE, return_value=DATA_RESPONSE) as data_mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.update(can_id)

        assert coe._channels[can_id] == {ChannelType.INPUT: {}}

        data_mock.assert_called_once()
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_update_data_received():
    """Test the update method with new data."""
    coe = CoE(TEST_HOST)

    can_id = 42

    assert coe._channels == {}
    assert coe.last_update == {}

    with patch(COE_DATA_PACKAGE, return_value=DATA_RESPONSE) as data_mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.update(can_id)

        assert coe._channels[can_id] == {
            ChannelMode.DIGITAL: {1: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")},
            ChannelMode.ANALOG: {1: CoEChannel(ChannelMode.ANALOG, 1, 34.4, "1")},
        }

        assert math.isclose(coe.last_update[can_id], 1680410064.03764)

        data_mock.assert_called_once()
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_update_data_received_multiple_ids():
    """Test the update method with new data with an existing other id."""
    coe = CoE(TEST_HOST)

    can_id = 42
    can_id2 = 31

    coe._channels[can_id2] = {
        ChannelMode.DIGITAL: {12: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")}
    }

    coe.last_update = {can_id: 0, can_id2: 1111111}

    assert coe._channels == {
        can_id2: {
            ChannelMode.DIGITAL: {12: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")}
        }
    }

    assert coe.last_update[can_id] == 0
    assert coe.last_update[can_id2] == 1111111

    with patch(COE_DATA_PACKAGE, return_value=DATA_RESPONSE) as data_mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.update(can_id)

        assert coe._channels[can_id] == {
            ChannelMode.DIGITAL: {1: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")},
            ChannelMode.ANALOG: {1: CoEChannel(ChannelMode.ANALOG, 1, 34.4, "1")},
        }

        assert coe._channels[can_id2] == {
            ChannelMode.DIGITAL: {12: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")}
        }

        assert math.isclose(coe.last_update[can_id], 1680410064.03764)

        assert math.isclose(coe.last_update[can_id2], 1111111)

        data_mock.assert_called_once()
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_update_data_received_with_empty_slots():
    """Test the update method with new data with empty slots."""
    coe = CoE(TEST_HOST)

    can_id = 42

    assert coe._channels == {}

    with patch(
        COE_DATA_PACKAGE, return_value=DATA_RESPONSE_WITH_EMPTY_SLOTS
    ) as data_mock, patch(COE_VERSION_CHECK_PACKAGE) as version_mock:
        await coe.update(can_id)

        assert coe._channels[can_id] == {
            ChannelMode.DIGITAL: {1: CoEChannel(ChannelMode.DIGITAL, 1, 1, "43")},
            ChannelMode.ANALOG: {
                1: CoEChannel(ChannelMode.ANALOG, 1, 34.4, "1"),
                3: CoEChannel(ChannelMode.ANALOG, 3, 3.5, "0"),
            },
        }

        data_mock.assert_called_once()
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_get_server_version():
    """Test the test_get_server_version."""
    coe = CoE(TEST_HOST)

    version = "1.1.0"

    with patch(COE_VERSION_PACKAGE, return_value=version) as version_mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_check_mock:
        result = await coe.get_server_version()

        assert result == version

        version_mock.assert_called_once()
        version_check_mock.assert_called_once()


@pytest.mark.asyncio
async def test_send_analog_values():
    """Test the send_analog_values."""
    coe = CoE(TEST_HOST)

    data = [CoEChannel(ChannelMode.ANALOG, 0, 1, "43")]
    page = 1

    with patch(COE_SEND_ANALOG_PACKAGE) as mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.send_analog_values(data, page)

        mock.assert_called_once_with(data, page)
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_send_digital_values():
    """Test the send_digital_values."""
    coe = CoE(TEST_HOST)

    data = [CoEChannel(ChannelMode.DIGITAL, 0, 1, "")]
    page = False

    with patch(COE_SEND_DIGITAL_PACKAGE) as mock, patch(
        COE_VERSION_CHECK_PACKAGE
    ) as version_mock:
        await coe.send_digital_values(data, page)

        mock.assert_called_once_with(data, page)
        version_mock.assert_called_once()


@pytest.mark.asyncio
async def test_check_version():
    """Test if the version check fetches the server version."""
    coe = CoE(TEST_HOST)

    with patch(COE_VERSION_PACKAGE, return_value="0.0.0") as version_mock:
        await coe._check_version()

        version_mock.assert_called_once()
