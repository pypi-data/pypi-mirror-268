# Copyright 2024 Gergo Nagy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class SystemFailure(Exception):
    """
    Exception raised for errors that are unrecoverable.
    This type of error results in termination of the program because it is not safe for the program to continue.
    """

    def __init__(
        self, message="System encountered an unrecoverable error. Terminating."
    ):
        self.message = message
        super().__init__(self.message)


class OperatorFailure(Exception):
    """
    Exception raised for recoverable errors caused by the operator.
    """

    def __init__(self, message="Operator encountered a recoverable error."):
        self.message = message
        super().__init__(self.message)


class ProviderFailure(Exception):
    """
    Exception raised for failures in the Kubernetes API calls.
    These errors can be recovered from.
    """

    def __init__(self, message="Kubernetes API call failed but can be recovered."):
        self.message = message
        super().__init__(self.message)


class UserFailure(Exception):
    """
    Exception raised for errors caused by the user.
    """

    def __init__(self, message="User error."):
        self.message = message
        super().__init__(self.message)
