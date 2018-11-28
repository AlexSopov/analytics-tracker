from werkzeug.exceptions import BadRequest

from app.tracker.handling.handlers import ClickHandlerStrategy, PurchaseHandlerStrategy

strategies_map = {
    'click': ClickHandlerStrategy(),
    'purchase': PurchaseHandlerStrategy()
}


def get_strategy(request):
    event_type = request.get('event')
    return strategies_map.get(event_type)
