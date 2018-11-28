from werkzeug.exceptions import BadRequest


class JSONLoadingBadRequest(BadRequest):
    def __init__(self, e):
        description = 'Failed to decode JSON object: {0}'.format(e)
        super().__init__(description)


class NonexistentProjectBadRequest(BadRequest):
    def __init__(self, project):
        description = "Project \"{project}\" doesn't exist.".format(project=project)
        super().__init__(description)


class NotSupportedEventTypeBadRequest(BadRequest):
    def __init__(self, event_type):
        description = 'Event type {type} is not supported'.format(type=event_type)
        super().__init__(description)
