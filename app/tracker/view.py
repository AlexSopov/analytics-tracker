from flask import Blueprint, request, Request, g
from werkzeug.exceptions import BadRequest

from app.tracker.handling import request_handler
from app.tracker.validations.wrappers import project_exists, track_schema_valid

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['POST'])
@track_schema_valid
@project_exists
def track(project):
    """
    Handles /track/<project> request. Validates data and inserts appropriate
    record to database.
    :param project: Project for which event is executed. Must exist in database.
    :return: 204 - no content on success
    400 - On not valid request body or project doesn't exist
    """
    post_body = request.get_json()

    return request_handler.handle(post_body, g.project)


def on_json_loading_failed(e):
    raise BadRequest('Failed to decode JSON object: {0}'.format(e))


Request.on_json_loading_failed = on_json_loading_failed
