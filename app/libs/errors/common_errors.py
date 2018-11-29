from flask import jsonify
from app.libs.errors.error_code import ErrorCode


class InvalidUsage(Exception):
    """
    Class representing internal error that can be serialized.
    Stores message of error, status code and internal sub-status.
    """
    status_code = 400

    def __init__(self, message, code, status_code=None):
        Exception.__init__(self)
        self.message = message
        self.code = code

        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return {
            'code': self.code,
            'message': self.message,
        }

    def to_response(self):
        response = jsonify(self.to_dict())
        response.status_code = self.status_code

        return response


class JSONLoadingBadRequest(InvalidUsage):
    def __init__(self, e):
        message = 'Failed to decode JSON object: {0}'.format(e)
        super().__init__(message, ErrorCode.JSON_LOADING_FAILED)


class NonexistentProjectBadRequest(InvalidUsage):
    def __init__(self, project):
        message = 'Project "{project}" does not exist.'.format(project=project)
        super().__init__(message, ErrorCode.PROJECT_DOES_NOT_EXIST)


class NotSupportedEventTypeBadRequest(InvalidUsage):
    def __init__(self, event_type):
        message = 'Event type "{type}" is not supported'.format(type=event_type)
        super().__init__(message, ErrorCode.NOT_SUPPORTED_EVENT_TYPE)
