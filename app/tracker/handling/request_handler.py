from app.libs.errors.common_errors import NotSupportedEventTypeBadRequest
from app.tracker.handling import handlers_collection


def handle(request_body, project):
    """
    Handles request represented by request_body. Selects appropriate
    strategy for handling request and routes execution to it.
    :param request_body: Body of POST request.
    :param project: Project for which handling is executed.
    :return: Result of handling. Returns 204 if request processed
    and BadRequest otherwise.
    """
    handler_strategy = handlers_collection.get_strategy(request_body)

    if handler_strategy is not None:
        return handler_strategy.handle(request_body, project)

    raise NotSupportedEventTypeBadRequest(request_body.get('event'))
