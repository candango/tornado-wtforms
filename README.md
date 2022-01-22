# Candango Tornado WTForms

[![Latest PyPI version](https://img.shields.io/pypi/v/tornado-wtforms.svg)](https://pypi.org/project/tornado-wtforms/)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/tornado-wtforms.svg)](https://pypi.org/project/tornado-wtforms/)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fcandango%2Ftornado-wtforms%2Fbadge&style=flat)](https://actions-badge.atrox.dev/candango/tornado-wtforms/goto)

WTForms extensions for Tornado forked from
[WTForms-Tornado](https://github.com/puentesarrin/wtforms-tornado).

We will derive the amazing work developed by the original project and add 
further improvements.

The project [WTForms-Tornado](https://github.com/puentesarrin/wtforms-tornado)
will continue to be matained. Check the original project to see if it fit the
needs your project/application needs.

## Usage

```python
import tornado.ioloop
import tornado.web

from wtforms.fields import IntegerField
from wtforms.validators import DataRequired
from tornado_wtforms.form import TornadoForm


class SumForm(TornadoForm):

   a = IntegerField(validators=[DataRequired()])
   b = IntegerField(validators=[DataRequired()])


class SumHandler(tornado.web.RequestHandler):
   def get(self):
       self.write("Hello, world")

   def post(self):
       form = SumForm(self.request.arguments)
       if form.validate():
           self.write(str(form.data['a'] + form.data['b']))
       else:
           self.set_status(400)
           self.write("" % form.errors)


application = tornado.web.Application([
    (r"/", SumHandler),
])

if __name__ == "__main__":
   application.listen(8888)
   tornado.ioloop.IOLoop.instance().start()
```

## Backwards Compatibility

We'll keep a backwards compatibility with the WTForms-Tornado but a
depreciation warning will be logged.

This still works after the instalation:

```python
from wtforms_tornado import Form

class LegacyForm(Form):

   pass
```

The `tornado_wtforms.from.Form` class is extending `wtforms.form.TornadoForm`
and is available to be imported at `wtforms_tornado` module.

Just changing wtforms_tornado by tornado_wtforms and keep importing Form won't
work, `from tornado_wtforms import Form`, because Form is not
referenced in tornado_wtforms module. Either you do
`from tornado_wtforms.form import TornadoForm` or
`from tornado_wtforms.form import Form`. The second option will still trigger
a depreciation after instantiating a Form instance.


## Installation

You can to use pip_ to install Tornado-WTForms:

```shell
$ pip install tornado-wtforms
```

Or using last source:

```shell
$ pip install git+git://github.com/puentesarrin/tornado-wtforms.git
```

Or manually, download the latest source from PyPI:

```shell
$ tar xvzf tornado-wtforms-$VERSION.tar.gz
$ cd tornado-wtforms-$VERSION
$ python setup.py build
$ sudo python setup.py install
```

## Support

Tornado WTForms is a fork from
[WTForms Tornado](https://pypi.org/project/wtforms-tornado/)
and now is one of
[Candango Open Source Group](http://www.candango.org/projects/)
initiatives and is available under
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

[WTForms Tornado](https://pypi.org/project/wtforms-tornado/) is maintained by
[Jorge Puente Sarrín](https://github.com/puentesarrin) and is available under
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

This web site and all documentation is licensed under [Creative
Commons 3.0](http://creativecommons.org/licenses/by/3.0/).

Copyright (c) 2022 Flávio Gonçalves Garcia

Copyright (c) 2013-2022 Jorge Puente Sarrín
