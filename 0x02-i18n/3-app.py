#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" adding a get locale function with the babel.localeselector decorator"""

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
def index() -> str:
    """ render simple hello world html file """
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """ get locale language code from request accepted languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
