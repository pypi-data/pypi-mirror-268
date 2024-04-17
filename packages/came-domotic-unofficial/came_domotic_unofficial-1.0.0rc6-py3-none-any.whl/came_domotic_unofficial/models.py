# Copyright 2024 - GitHub user: fredericks1982

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from dataclasses import dataclass
from typing import Optional

from .auth import Auth


class CameEntity:
    """Base class for all the CAME entities."""


class CameUser(CameEntity):
    """Represents a user object in the CameDomotic API."""

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize a light object."""
        if raw_data is None or "name" not in raw_data:
            raise ValueError(
                "raw_data must be a dictionary, containing the 'name' key."
            )
        self.raw_data: dict = raw_data
        self.auth: Auth = auth

    # Note: each property name maps the name in the returned data

    @property
    def name(self) -> int:
        """Return the name of the user."""
        return self.raw_data["name"]


@dataclass
class CameFeature(CameEntity):
    """Represents a feature object in the CameDomotic API."""

    name: str


@dataclass
class CameServerInfo(CameEntity):
    """Represents the server information in the CameDomotic API."""

    keycode: str
    serial: str
    swver: Optional[str] = None
    type: Optional[str] = None
    board: Optional[str] = None


class CameLight(CameEntity):
    """Represents a light object in the CameDomotic API."""

    def __init__(self, raw_data: dict, auth: Auth):
        """Initialize a light object."""
        self.raw_data: dict = raw_data
        self.auth: Auth = auth

    # Note: each property name maps the name in the returned data

    @property
    def act_id(self) -> int:
        """Return the ID of the light."""
        return self.raw_data["act_id"]

    @property
    def floor_ind(self) -> int:
        """Return the floor index of the light."""
        return self.raw_data["floor_ind"]

    @property
    def name(self) -> str:
        """Return the name of the light."""
        return self.raw_data["name"]

    @property
    def room_ind(self) -> int:
        """Return the room index of the light."""
        return self.raw_data["room_ind"]

    @property
    def status(self) -> int:
        """Return the status of the light (1: ON, 0: OFF)."""
        return self.raw_data["status"]

    @property
    def type(self) -> str:
        """Return the type of the light (STEP_STEP: normal, DIMMER: dimmable)."""
        return self.raw_data["type"]

    @property
    def perc(self) -> int:
        """Return the brightness percentage of the light (range: 0-100).

        Non dimmable lights will always return 100.
        """
        return self.raw_data.get("perc", 100)

    async def async_set_status(self, status: int, brightness: Optional[int] = None):
        """Control the light."""

        client_id = await self.auth.async_get_valid_client_id()
        payload = {
            "sl_appl_msg": {
                "act_id": self.act_id,
                "client": client_id,
                "cmd_name": "light_switch_req",
                "cseq": self.auth.cseq + 1,
                "wanted_status": status,
                # "perc": 80, # added conditionally by the logic below
            },
            "sl_appl_msg_type": "domo",
            "sl_client_id": client_id,
            "sl_cmd": "sl_data_req",
        }

        if isinstance(brightness, int) and self.type == "DIMMER":
            uploading_brightness = True
            normalized_brightness = max(0, min(brightness, 100))
            payload["sl_appl_msg"]["perc"] = normalized_brightness
        else:
            uploading_brightness = False

        await self.auth.async_send_command(payload)

        # Update the status of the light if everything went as expected
        self.raw_data["status"] = status
        if uploading_brightness:
            self.raw_data["perc"] = normalized_brightness


# Openings
# Scenarios
# Digital inputs
