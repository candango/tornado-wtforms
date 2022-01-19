#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2022 Flávio Gonçalves Garcia
# Copyright 2013-2022 Jorge Puente Sarrín
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from tests import application_test, wraper_test


def suite():
    test_loader = unittest.TestLoader()
    alltests = unittest.TestSuite()
    alltests.addTests(test_loader.loadTestsFromModule(application_test))
    alltests.addTests(test_loader.loadTestsFromModule(wraper_test))
    return alltests


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite())
    if not result.wasSuccessful():
        exit(2)

