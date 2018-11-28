import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('analytics-tracker')
app.secret_key = os.urandom(24)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.tracker.view import track_blueprint
app.register_blueprint(track_blueprint, url_prefix='/')

from app.tracker.models import data_models