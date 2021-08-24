# coding: utf-8
import os
from flask import Flask

__version__ = "0.4.1"
app = Flask(__name__)
app.config.update(SECRET_KEY=os.urandom(24))
app.config["SESSION_TYPE"] = "filesystem"


import mockidp.saml.routes
import mockidp.routes
