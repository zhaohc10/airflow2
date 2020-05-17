# coding: utf-8
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

from __future__ import unicode_literals

import warnings

from testinfra.host import get_host
from testinfra.host import get_hosts


def get_backend(hostspec, **kwargs):
    warnings.warn("get_backend() is deprecated, use get_host() instead",
                  DeprecationWarning, stacklevel=2)
    return get_host(hostspec, **kwargs).backend


def get_backends(hosts, **kwargs):
    warnings.warn("get_backends() is deprecated, use get_hosts() instead",
                  DeprecationWarning, stacklevel=2)
    return [host.backend for host in get_hosts(hosts, **kwargs)]