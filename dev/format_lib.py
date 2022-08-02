#!/usr/bin/env python3
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

"""Erlang formatter lib for CouchDB
Warning: this file is not meant to be executed manually
"""

import pathlib
import subprocess


def get_source_paths():
    for item in (
        subprocess.run(
            ["git", "ls-files"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        .stdout.decode("utf-8")
        .split("\n")
    ):
        item_path = pathlib.Path(item)
        if item_path.suffix != ".erl":
            continue

        yield {
            "raw_path": item,
            "item_path": item_path,
        }
