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


class CameDomoticError(Exception):
    """Base exception class for the Came Domotic package."""


class CameDomoticServerNotFoundError(CameDomoticError):
    """Raised when the specified host is not available"""


# Authentication exception class
class CameDomoticAuthError(CameDomoticError):
    """Raised when there is an authentication error with the remote server."""


# Server exception class
class CameDomoticServerError(CameDomoticError):
    """Error raised when interacting the remote Came Domotic server"""

    @staticmethod
    def format_ack_error(ack_code: str = "N/A", reason: str = "N/A") -> str:
        """Formats the ack code and reason in a human-readable format.

        :param ack_code: the ack code returned by the server (optional).
        :param reason: the reason returned by the server (optional).
        :return: a human-readable string with the ack code and reason.
        """

        # Convert with str() to ensure that will never raise an exception
        return f"Bad ack code: {str(ack_code)} - Reason: {str(reason)}"
