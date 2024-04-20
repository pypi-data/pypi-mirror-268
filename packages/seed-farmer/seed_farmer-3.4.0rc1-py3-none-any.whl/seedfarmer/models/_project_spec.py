#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License").
#    You may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from typing import Optional, Union

from seedfarmer.models._base import CamelModel


class ProjectSpec(CamelModel):
    """
    ProjectSpec
    This represents the project configuration specification. This class is
    typically populated from the project's top-level seedfarmer.yaml file.
    """

    project: str
    description: Optional[str] = None
    project_policy_path: Optional[str] = None
    seedfarmer_version: Optional[Union[int, str]] = None
