from flask import Blueprint, request, Request, g

from app.tracker.handling import request_handler
from app.tracker.validations.wrappers import project_exists, track_schema_valid

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['POST'])
@project_exists
@track_schema_valid
def track(project):
    """
    Handles '/track/<project>' request. Validates data and inserts appropriate
    record to database.

    :param project: Project for which event is executed. Must exist in database.
    :return: 204 - no content on success
    400 - On not valid request body or if project doesn't exist
    """
    post_body = request.get_json()

    return request_handler.handle(post_body, g.project)

