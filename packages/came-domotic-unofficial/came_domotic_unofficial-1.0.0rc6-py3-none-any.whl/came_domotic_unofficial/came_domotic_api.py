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

import json
from typing import List

from .auth import Auth
from .models import CameFeature, CameServerInfo, CameUser, CameLight


class CameDomoticAPI:
    """Class to interact with Came Domotic API."""

    def __init__(self, auth: Auth):
        self.auth = auth

    async def async_get_users(self) -> List[CameUser]:
        """Get the list of users."""

        client_id = await self.auth.async_get_valid_client_id()
        payload = {"sl_client_id": client_id, "sl_cmd": "sl_users_list_req"}

        response = await self.auth.async_send_command(payload)
        json_response = await response.json(content_type=None)

        return [CameUser(user, self.auth) for user in json_response["sl_users_list"]]

    async def async_get_features(self):
        """Get the list of features."""

        client_id = await self.auth.async_get_valid_client_id()
        payload = {
            "sl_appl_msg": {
                "client": client_id,
                "cmd_name": "feature_list_req",
                "cseq": self.auth.cseq + 1,
            },
            "sl_appl_msg_type": "domo",
            "sl_client_id": client_id,
            "sl_cmd": "sl_data_req",
        }
        response = await self.auth.async_send_command(payload)
        json_response = await response.json(content_type=None)

        return [CameFeature(name) for name in json_response["list"]]

    async def async_get_server_info(self):
        """Get the server information."""

        client_id = await self.auth.async_get_valid_client_id()
        payload = {
            "sl_appl_msg": {
                "client": client_id,
                "cmd_name": "feature_list_req",
                "cseq": self.auth.cseq + 1,
            },
            "sl_appl_msg_type": "domo",
            "sl_client_id": client_id,
            "sl_cmd": "sl_data_req",
        }
        response = await self.auth.async_send_command(payload)
        json_response = await response.json(content_type=None)

        return CameServerInfo(
            keycode=json_response["keycode"],
            swver=json_response["swver"],
            type=json_response["type"],
            board=json_response["board"],
            serial=json_response["serial"],
        )

    async def async_get_status_udates(self):
        """Get the list of status updates."""
        # TODO Get the list of status updates
        pass

    async def async_get_lights(self) -> List[CameLight]:
        """Get the list of devices."""

        client_id = await self.auth.async_get_valid_client_id()
        payload = {
            "sl_appl_msg": {
                "client": client_id,
                "cmd_name": "light_list_req",
                "cseq": self.auth.cseq + 1,
                "topologic_scope": "plant",
                "value": 0,
            },
            "sl_appl_msg_type": "domo",
            "sl_client_id": client_id,
            "sl_cmd": "sl_data_req",
        }
        response = await self.auth.async_send_command(payload)
        json_response = await response.json(content_type=None)

        return [CameLight(light, self.auth) for light in json_response["array"]]
