from shipping_strategy import ShippingStrategy
from shipping_result import ShippingResult

class StandardShipping(ShippingStrategy):

    def calculate_shipping(self, request):
   
        weight = request.weight

        distance = request.distance

        cost = weight * 2 + distance * 0.5

        return  ShippingResult(cost)
