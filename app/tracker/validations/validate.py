import functools

from werkzeug.exceptions import BadRequest

from app.tracker.models.project import Project
from app.tracker.validations.schema import required, of_type, is_valid


def project_exists(func):

    @functools.wraps(func)
    def wrapper_project_exists(*args, **kwargs):
        project_name = kwargs.get('project')
        project_data = Project.query.get(project_name)

        if project_data is None:
            raise BadRequest("Project \"{0}\" doesn't exist.".format(project_name))

        return func(*args, **kwargs)

    return wrapper_project_exists


def validate_track_post_body(post_body):
    schema = {
        'event': [required, of_type(str)],
        'data': [required, of_type(dict)],
    }

    return is_valid(schema, post_body)
