# Copyright (c) 2010 OpenStack, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from webob import Request

from swift.common import healthcheck


class TestHealthCheck(unittest.TestCase):

    def test_healthcheck(self):
        controller = healthcheck.HealthCheckController()
        req = Request.blank('/any/path', environ={'REQUEST_METHOD': 'GET'})
        resp = controller.GET(req)
        self.assertEquals(resp.status_int, 200)


if __name__ == '__main__':
    unittest.main()