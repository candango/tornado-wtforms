# Candango Tornado WTForms

[![Latest PyPI version](https://img.shields.io/pypi/v/tornado-wtforms.svg)](https://pypi.org/project/tornado-wtforms/)
[![Number of PyPI downloads](https://img.shields.io/pypi/dm/tornado-wtforms.svg)](https://pypi.org/project/tornado-wtforms/)

WTForms extensions for Tornado forked from [WTForms-Tornado](https://github.com/puentesarrin/wtforms-tornado).

## Usage

```python
import tornado.ioloop
import tornado.web

from wtforms.fields import IntegerField
from wtforms.validators import Required
from wtforms_tornado import Form

class SumForm(Form):

   a = IntegerField(validators=[Required()])
   b = IntegerField(validators=[Required()])

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

Tornado WTForms is a fork from [WTForms Tornado](https://pypi.org/project/wtforms-tornado/)
and now is one of [Candango Open Source Group](http://www.candango.org/projects/)
initiatives. It is available under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).

This web site and all documentation is licensed under [Creative
Commons 3.0](http://creativecommons.org/licenses/by/3.0/).

Copyright (c) 2022 Flávio Gonçalves Garcia

Copyright (c) 2013-2022 Jorge Puente Sarrín
