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


"""
CAME Domotic helpers (enums, mappers, etc.)
"""

from typing import Type
from .came_entity import CameEntity_OLD
from .feature import Feature_OLD
from .light import Light_OLD
from .opening import Opening_OLD
from .digital_input import DigitalInput_OLD
from .scenario import Scenario_OLD
from .enums import EntityType_OLD


# region Mappers

_EntityType2Class: dict[EntityType_OLD, Type[CameEntity_OLD]] = {
    EntityType_OLD.FEATURES: Feature_OLD,
    EntityType_OLD.LIGHTS: Light_OLD,
    EntityType_OLD.OPENINGS: Opening_OLD,
    EntityType_OLD.DIGITALIN: DigitalInput_OLD,
    EntityType_OLD.SCENARIOS: Scenario_OLD,
    # EntityType.UPDATE:
    # EntityType.RELAYS:
    # EntityType.CAMERAS:
    # EntityType.TIMERS:
    # EntityType.THERMOREGULATION:
    # EntityType.ANALOGIN:
    # EntityType.USERS:
    # EntityType.MAPS:
}

_Class2SwitchCommand = {
    Light_OLD: "light_switch_req",
    Opening_OLD: "opening_move_req",
    Scenario_OLD: "scenario_activation_req",
}

# endregion
