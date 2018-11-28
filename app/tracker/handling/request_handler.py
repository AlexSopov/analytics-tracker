from werkzeug.exceptions import BadRequest

from app.tracker.handling import handlers_collection


def handle(request_body, project):
    handler_strategy = handlers_collection.get_strategy(request_body)

    if handler_strategy is not None:
        return handler_strategy.handle(request_body, project)

    raise BadRequest('Event type {type} is not supported'
                     .format(type=request_body.get('event')))
