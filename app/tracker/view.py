from flask import Blueprint

track_blueprint = Blueprint('track', __name__)


@track_blueprint.route("/track/<string:project>", methods=['GET'])
def get_all(project):
    return project
