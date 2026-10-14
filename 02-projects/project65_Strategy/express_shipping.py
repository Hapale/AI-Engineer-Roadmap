from shipping_strategy import ShippingStrategy
from shipping_result import ShippingResult

class ExpressShipping(ShippingStrategy):


    def calculate_shipping(self, request):
   
        weight = request.weight

        distance = request.distance

        cost = weight * 3 + distance * 1

        return  ShippingResult(cost)