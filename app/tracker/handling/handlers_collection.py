from werkzeug.exceptions import BadRequest

from app.tracker.handling.handlers import ClickHandler, PurchaseHandler

strategies_map = {
    'click': ClickHandler(),
    'purchase': PurchaseHandler()
}


def get_strategy(request):
    event_type = request.get('event')
    return strategies_map.get(event_type)
