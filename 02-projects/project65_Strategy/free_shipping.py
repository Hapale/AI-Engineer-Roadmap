from shipping_strategy import ShippingStrategy
from shipping_result import ShippingResult

class FreeShipping(ShippingStrategy):

    def calculate_shipping(self, request):
        return ShippingResult(0)
    