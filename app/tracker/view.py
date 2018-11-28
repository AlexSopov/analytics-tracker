from flask import Blueprint, request, Request
from werkzeug.exceptions import BadRequest

from app.tracker.handling import request_handler
from app.tracker.validations.wrappers import project_exists, track_schema_valid

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['POST'])
@track_schema_valid
@project_exists
def track(project):
    post_body = request.get_json()

    return request_handler.handle(post_body, project)


def on_json_loading_failed(e):
    raise BadRequest('Failed to decode JSON object: {0}'.format(e))


Request.on_json_loading_failed = on_json_loading_failed
