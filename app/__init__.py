import os
from flask import Flask, Request
from flask.json import jsonify
from werkzeug.exceptions import BadRequest

from app.libs.errors.common_errors import JSONLoadingBadRequest
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


def on_json_loading_failed(self, e):
    raise JSONLoadingBadRequest(e)


@app.errorhandler(BadRequest)
def badrequest_handler(error):
    response = jsonify({
        'description': error.description,
    })
    response.status_code = error.code

    return response


Request.on_json_loading_failed = on_json_loading_failed
