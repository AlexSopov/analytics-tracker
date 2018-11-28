from abc import ABC, abstractmethod

from app.lib.response.response import no_content


class HandlerBase(ABC):
    @abstractmethod
    def handle(self, request_body, project):
        pass


class ClickHandler(HandlerBase):
    def handle(self, request_body, project):
        return no_content()


class PurchaseHandler(HandlerBase):
    def handle(self, request_body, project):
        return no_content()