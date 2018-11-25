from flask import Blueprint

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track", methods=['GET'])
def get_all():
    return ""
