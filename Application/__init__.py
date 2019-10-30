from flask import Flask
from flask_cors import CORS

import os,logging

app = Flask(__name__)
app.secret_key = 'qwertyuiopasdfghjklzxcvbnm123456'#os.urandom(24) 

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

CORS(app)


# Configuring Routes

from Application.views.loginview import applogin
app.register_blueprint(applogin)

from Application.views.view import appview
app.register_blueprint(appview)

