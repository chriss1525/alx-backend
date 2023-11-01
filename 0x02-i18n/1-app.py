#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" simple flask app that renders html file,\
import Babel and configure our app to use it """
from flask_babel import Babel
from flask import *

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Configure available languages in our app """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ render html file """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
