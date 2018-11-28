from werkzeug.exceptions import BadRequest

from app.tracker.handling import handlers_collection


def handle(request_body, project):
    """
    Handles request represented by request_body. Selects appropriate
    strategy for handling request and routes execution to is.
    :param request_body: Body of POST request.
    :param project: Project for which handling is executed.
    :return: Result of handling. Returns 204 if request processes
    and BadRequest otherwise.
    """
    handler_strategy = handlers_collection.get_strategy(request_body)

    if handler_strategy is not None:
        return handler_strategy.handle(request_body, project)

    raise BadRequest('Event type {type} is not supported'
                     .format(type=request_body.get('event')))
