from flask import Blueprint, request, Request
from werkzeug.exceptions import BadRequest

from app.lib.response.response import no_content
from app.tracker.handlers import request_handler
from app.tracker.validations.validate import project_exists, validate_track_post_body

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['POST'])
@project_exists
def track(project):
    post_body = request.get_json()

    if not validate_track_post_body(post_body):
        raise BadRequest()

    return request_handler.handle(post_body, project)


def on_json_loading_failed(self, e):
    raise BadRequest('Failed to decode JSON object: {0}'.format(e))


Request.on_json_loading_failed = on_json_loading_failed
