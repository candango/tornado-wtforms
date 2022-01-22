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
from wtforms.fields import Field, _unset_value
try:
    from wtforms.fields import StringField
    from wtforms.validators import DataRequired
except ImportError:
    from wtforms.fields import TextField as StringField
    from wtforms.validators import Required as DataRequired
from tornado.httputil import HTTPServerRequest

from tornado_wtforms.form import TornadoInputWrapper, TornadoForm


class SneakyField(Field):
    def __init__(self, sneaky_callable, *args, **kwargs):
        super(SneakyField, self).__init__(*args, **kwargs)
        self.sneaky_callable = sneaky_callable

    def process(self, formdata, data=_unset_value):
        self.sneaky_callable(formdata)


class _Connection(object):
    def __init__(self, context):
        self.context = context


class _Context(object):
    remote_ip = None


class TornadoWrapperTest(unittest.TestCase):
    def setUp(self):
        connection = _Connection(_Context())
        self.test_values = HTTPServerRequest(
            'GET', 'http://localhost?a=Apple&b=Banana&a=Cherry',
            connection=connection
        )
        self.empty_mdict = TornadoInputWrapper({})
        self.filled_mdict = TornadoInputWrapper(self.test_values.arguments)

    def test_automatic_wrapping(self):
        def _check(formdata):
            self.assertTrue(isinstance(formdata, TornadoInputWrapper))

        form = TornadoForm({'a': SneakyField(_check)})
        form.process(self.filled_mdict)

    def test_empty(self):
        formdata = TornadoInputWrapper(self.empty_mdict)
        self.assertFalse(formdata)
        self.assertEqual(len(formdata), 0)
        self.assertEqual(list(formdata), [])
        self.assertEqual(formdata.getlist('fake'), [])

    def test_filled(self):
        formdata = TornadoInputWrapper(self.filled_mdict)
        self.assertTrue(formdata)
        self.assertEqual(len(formdata), 2)
        self.assertEqual(sorted(list(formdata)), sorted(['a', 'b']))
        self.assertTrue('b' in formdata)
        self.assertTrue('fake' not in formdata)
        self.assertEqual(formdata.getlist('a'), ['Apple', 'Cherry'])
        self.assertEqual(formdata.getlist('b'), ['Banana'])
        self.assertEqual(formdata.getlist('fake'), [])
