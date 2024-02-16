#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
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
#
from ..runschema.calculation import Calculation
from ..runschema.method import Method
from ..runschema.run import Run
from ..runschema.system import System


def test_schema():
    run = Run()
    assert run.m_def.definition_id == 'fc17fdfdcba5aef2c02835a81ed65f95f314b687'
    run.calculation.append(Calculation())
    run.method.append(Method())
    run.system.append(System())
