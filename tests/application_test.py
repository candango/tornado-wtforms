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

from tests import TEST_ROOT
import os
try:
    from wtforms.fields import StringField
    from wtforms.validators import DataRequired
except ImportError:
    from wtforms.fields import TextField as StringField
    from wtforms.validators import Required as DataRequired
from tornado import locale, web, testing
from tornado_wtforms.form import TornadoForm


class SearchForm(TornadoForm):
    search = StringField(validators=[DataRequired('Search field is required')])


class DummyHandler(web.RequestHandler):
    def get_user_locale(self):
        return locale.get(self.get_argument('locale', 'en_US'))

    def get(self):
        form = SearchForm(self.request.arguments, locale_code=self.locale.code)
        if bool(self.get_argument('label', False)):
            self.finish(form.search.label.text)
        else:
            if form.validate():
                self.finish(form.data)
            else:
                self.set_status(500)
                self.finish(form.errors)


class TornadoApplicationTest(testing.AsyncHTTPTestCase):
    def setUp(self):
        super(TornadoApplicationTest, self).setUp()
        locale.load_translations(os.path.join(TEST_ROOT, "translations"))

    def get_app(self):
        return web.Application([('/', DummyHandler)])

    def test_successful_form(self):
        response = self.fetch('/?search=wtforms&page=2')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'{"search": "wtforms"}')

    def test_wrong_form(self):
        try:
            response = self.fetch('/?fake=wtforms')
        except:
            print("buga")
        self.assertEqual(response.code, 500)
        self.assertEqual(response.body,
                         b'{"search": ["Search field is required"]}')

    def test_translations_default(self):
        response = self.fetch('/?label=True&search=wtforms')
        self.assertEqual(response.body, b'Search')

    def test_translations_en(self):
        response = self.fetch('/?locale=en_US&label=True&search=wtforms')
        self.assertEqual(response.body, b'Search')

    def test_translations_es(self):
        response = self.fetch('/?locale=es_ES&label=True&search=wtforms')
        self.assertEqual(response.body, b'B\xc3\xbasqueda')
