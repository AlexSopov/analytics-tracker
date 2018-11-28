from abc import ABC, abstractmethod


class HandlerBase(ABC):
    @abstractmethod
    def handle(self, request_body):
        pass


class ClickHandler(HandlerBase):
    def handle(self, request_body):
        pass


class PurchaseHandler(HandlerBase):
    def handle(self, request_body):
        pass