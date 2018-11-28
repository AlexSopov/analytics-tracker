from werkzeug.exceptions import BadRequest

from app.lib.response.response import no_content
from app.tracker.handlers import handlers_collection


def handle_request(request_body):
    handler_strategy = handlers_collection.get_strategy(request_body)

    if handler_strategy is not None:
        return handler_strategy.handle(request_body)

    raise BadRequest()
