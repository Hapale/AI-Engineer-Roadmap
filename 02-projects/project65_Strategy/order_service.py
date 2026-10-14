from shipping_strategy import ShippingStrategy
from shipping_request import ShippingRequest

class OrderService:
    def __init__(self, strategy:ShippingStrategy):

        self.strategy = strategy

    def calculate_shipping(self, request:ShippingRequest):

       return self.strategy.calculate_shipping(request)