from flask import Blueprint, request, g

from app.tracker.handling import request_handler
from app.tracker.validations.wrappers import validate_project_exists, validate_track_schema


track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['POST'])
@validate_project_exists
@validate_track_schema
def track(project):
    """
    Handles '/track/<project>' request. Validates data and inserts appropriate
    record to database.

    :param project: Project for which event is executed. Must exist in database.
    :return: 204 - no content on success
    400 - On not valid request body or if project doesn't exist
    """
    post_body = request.get_json(force=True)

    return request_handler.handle(post_body, g.project)
