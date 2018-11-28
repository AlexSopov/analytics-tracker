from abc import ABC, abstractmethod

from app.lib.response.response import no_content
from app.tracker.validations.schema import click_data_schema, purchase_data_schema
from app.tracker.validations.wrappers import validate_data


class HandlerBase(ABC):
    @abstractmethod
    def handle(self, request_body, project):
        pass


class ClickHandler(HandlerBase):
    @validate_data(click_data_schema())
    def handle(self, request_body, project):
        return no_content()


class PurchaseHandler(HandlerBase):
    @validate_data(purchase_data_schema())
    def handle(self, request_body, project):
        return no_content()