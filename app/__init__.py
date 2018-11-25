import os
from flask import Flask

app = Flask('analytics-tracker')
app.secret_key = os.urandom(24)
