import functools

from flask import request, g
from werkzeug.exceptions import BadRequest

from app import db
from app.lib.errors.common_errors import NonexistentProjectBadRequest
from app.lib.validations.validators import is_valid
from app.tracker.models.data_models import Project
from app.tracker.validations.schema import track_schema


def track_schema_valid(func):
    """
    Checks if format of post request for /track endpoint is valid.
    :param func: Function to be wrapped
    :return: Wrapped function executing result if data is valid, otherwise
    raises BadRequest.
    """
    schema = track_schema()

    @functools.wraps(func)
    def wrapper_track_schema_valid(*args, **kwargs):
        if is_valid(schema, request.get_json()):
            return func(*args, **kwargs)

        raise BadRequest()

    return wrapper_track_schema_valid


def project_exists(func):
    """
    Checks if requested project exist.
    :param func: Function to be wrapped
    :return: Result of validating if project exists.
    """

    @functools.wraps(func)
    def wrapper_project_exists(*args, **kwargs):
        project_name = kwargs.get('project')
        project_data = db.session.query(Project).get(project_name)

        if project_data is None:
            raise NonexistentProjectBadRequest(project_name)

        g.project = project_data
        return func(*args, **kwargs)

    return wrapper_project_exists


def validate_data(schema):
    """
    Validates that request's 'data' specifies appropriate schema.
    :param schema: Expected schema. The schema for which request_body is compared.
    :return: Wrapped function executing result if data is valid, otherwise
    raises BadRequest.
    """

    def wrapper_validate_schema(func):

        @functools.wraps(func)
        def wrapped(self, request_body, project):
            if is_valid(schema, request_body['data']):
                return func(self, request_body, project)

            raise BadRequest()

        return wrapped

    return wrapper_validate_schema
