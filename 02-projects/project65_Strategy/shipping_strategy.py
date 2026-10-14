from abc import ABC, abstractmethod
from shipping_request import ShippingRequest

class ShippingStrategy(ABC):

    @abstractmethod
    def calculate_shipping(self, request: ShippingRequest):
         pass