import os
from flask import Flask
from config import Config

app = Flask('analytics-tracker')
app.secret_key = os.urandom(24)
app.config.from_object(Config)

from app.tracker.view import track_blueprint
app.register_blueprint(track_blueprint, url_prefix='/')
