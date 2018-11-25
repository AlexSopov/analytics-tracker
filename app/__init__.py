import os
from flask import Flask

app = Flask('analytics-tracker')
app.secret_key = os.urandom(24)


from app.tracker.view import track_blueprint
app.register_blueprint(track_blueprint, url_prefix='/')
