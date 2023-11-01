#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" simple flask app that renders html file"""
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ render html file """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
