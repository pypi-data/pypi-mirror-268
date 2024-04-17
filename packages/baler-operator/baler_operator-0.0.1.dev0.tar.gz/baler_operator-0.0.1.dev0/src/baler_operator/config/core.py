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

# Core API constants
# Used for apiGroup, apiVersion in Kubernetes API CRD
__OPERATOR_API_BASE_URL__ = "baler.gatecastle.com"
__OPERATOR_API_VERSION__ = "v1"
# Pipeline APU
__OPERATOR_API_PIPELINE__ = f"pipelines.{__OPERATOR_API_BASE_URL__}"
# Used for kind in Kubernetes API CRD
__OPERATOR_KIND_HAYSTACK_SINGULAR__ = "haystack"
__OPERATOR_KIND_HAYSTACK_PLURAL__ = "haystacks"
