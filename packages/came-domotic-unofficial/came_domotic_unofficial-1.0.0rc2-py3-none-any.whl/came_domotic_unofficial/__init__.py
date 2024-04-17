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

import sys
import logging
from importlib.metadata import version, PackageNotFoundError

from .auth import Auth
from .came_domotic_api import CameDomoticAPI
from .errors import (
    CameDomoticAuthError,
    CameDomoticError,
    CameDomoticServerError,
    CameDomoticServerNotFoundError,
)

# Get the package version
try:
    __version__ = version(__package__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

# region Logging

# Create a logger for the package
_LOGGER = logging.getLogger(__package__)
_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s - "
    "%(module)s:%(lineno)d (%(funcName)s)"
)
_console_handler = logging.StreamHandler(sys.stdout)
_console_handler.setFormatter(_formatter)
_LOGGER.addHandler(_console_handler)
_LOGGER.setLevel(logging.DEBUG)


def get_logger():
    """
    Allows to set the log level and other properties from the calling code.

    Returns:
        Logger: The package logger
    """
    return _LOGGER


# endregion
