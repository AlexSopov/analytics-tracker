from abc import ABC, abstractmethod

from app import db
from app.libs.response.response import no_content
from app.tracker.models.data_models import ClickEvent
from app.tracker.validations.schema import click_data_schema, purchase_data_schema
from app.tracker.validations.wrappers import validate_data


class HandlerStrategyBase(ABC):

    """Base class for handling requests of specific event_type.
    Validates data from post body and creates appropriate record
    in database.
    """

    request_body_data = ''

    @abstractmethod
    def handle(self, request_body, project):
        self.request_body_data = request_body['data']
        pass

    def get_data_attribute(self, attribute):
        return self.request_body_data[attribute]


class ClickHandlerStrategy(HandlerStrategyBase):

    @validate_data(click_data_schema())
    def handle(self, request_body, project):
        super().handle(request_body, project)

        click_event = ClickEvent(project, self.get_data_attribute('track_id'))

        db.session.add(click_event)
        db.session.commit()

        return no_content()


class PurchaseHandlerStrategy(HandlerStrategyBase):

    @validate_data(purchase_data_schema())
    def handle(self, request_body, project):
        super().handle(request_body, project)

        db.session.add(ClickEvent(project, self.get_data_attribute('customer_id')))
        db.session.commit()

        return no_content()
