# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hashlib
import os
import pathlib
import sys
import time
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.request import urlopen

from nvidia_stub._vendor.packaging.tags import (
    interpreter_name,
    interpreter_version,
    platform_tags,
)
from nvidia_stub._vendor.packaging.utils import canonicalize_name, parse_wheel_filename
from nvidia_stub.common import parse_metadata
from nvidia_stub.error import report_install_failure

NVIDIA_PIP_INDEX_URL = os.environ.get("NVIDIA_PIP_INDEX_URL", "https://pypi.nvidia.com")
NVIDIA_STUB_NO_PIP = os.environ.get("NVIDIA_STUB_NO_PIP", False)


class WheelFilter(HTMLParser):
    """Parse PEP 503 index page to get the list of wheels and their sha256."""

    def __init__(self, *, convert_charrefs: bool = True) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.wheel_files = []

    def handle_starttag(self, tag, attrs) -> None:
        if tag == "a":
            for name, value in attrs:
                if name == "href" and value is not None:
                    if "#sha256=" in value:
                        wheel, sha = value.split("#sha256=")
                        self.wheel_files.append((wheel, sha))


def urlopen_with_retry(url, num_retries=4, **kwargs):
    """Retry HTTP call with backoff"""
    for i in range(1, num_retries + 1):
        try:
            return urlopen(url, **kwargs)
        except URLError:
            if i == num_retries:
                raise
        time.sleep(1.2**i)


def is_compatible_tag(tag, this_interp_tag, system_tags):
    if tag.abi == "none":
        if tag.interpreter in ["py3", this_interp_tag]:
            return tag.platform in system_tags
        else:
            return False
    elif tag.abi == this_interp_tag:
        # If the ABI is for this interpreter, the interpreter tag must be this interpreters
        if tag.interpreter != this_interp_tag:
            return False
    elif tag.abi == "abi3":
        # Any interpreter abi less than ours is acceptable for the stable ABI
        wheel_interp = tag.interpreter
        if wheel_interp.startswith("cp3"):
            interp_minor_version = wheel_interp[3:]
            if int(interp_minor_version) > sys.version_info.minor:
                return False
        else:
            return False
    if tag.platform in system_tags:
        return True
    return False


def get_compatible_wheel(wheel_files, version):
    system_tags = list(platform_tags())
    interp_name = interpreter_name()
    interp_version = interpreter_version()
    this_interp_tag = f"{interp_name}{interp_version}"
    for wheel, sha in wheel_files:
        _name, ver, _build_num, tags = parse_wheel_filename(wheel)
        if str(ver) != version:
            continue
        # tags is a frozenset since there *can* be compressed tags,
        # e.g. manylinux2014_x86_64.manylinux_2_28_x86_64
        for tag in tags:
            if is_compatible_tag(tag, this_interp_tag, system_tags):
                return wheel, sha
    return None, None


def download_manual(wheel_directory, distribution, version):
    index_response = urlopen_with_retry(f"{NVIDIA_PIP_INDEX_URL}/{distribution}/")
    html = index_response.read().decode("utf-8")
    parser = WheelFilter()
    parser.feed(html)
    # TODO: should we support multiple compatible wheels?
    wheel, sha = get_compatible_wheel(parser.wheel_files, version)
    if wheel is None:
        raise RuntimeError(f"Didn't find wheel for {distribution} {version}")
    wheel_url = f"{NVIDIA_PIP_INDEX_URL}/{distribution}/{wheel}"
    print(f"Downloading wheel {wheel}")
    wheel_response = urlopen_with_retry(wheel_url)
    file_hash = hashlib.sha256()
    with open(wheel_directory / wheel, "wb") as f:
        CHUNK = 16 * 1024
        while True:
            data = wheel_response.read(CHUNK)
            if not data:
                break
            file_hash.update(data)
            f.write(data)
    assert (
        file_hash.hexdigest() == sha
    ), f"Downloaded wheel and SHA256 don't match! {file_hash.hexdigest()}, {sha}"
    return wheel


def get_metadata_from_pkg_info(src_dir):
    with open(src_dir / "PKG-INFO") as f:
        pkg_info = f.read()
    return parse_metadata(pkg_info)


def download_wheel(wheel_directory, config_settings):
    src_dir = pathlib.Path(os.getcwd())
    metadata = get_metadata_from_pkg_info(src_dir)
    distribution = canonicalize_name(metadata["Name"])
    version = metadata["Version"]
    if metadata["Stub-Only"] == "True":
        report_install_failure(distribution, version, None)
    try:
        return download_manual(wheel_directory, distribution, version)
    except Exception as exception_context:
        report_install_failure(distribution, version, exception_context)
