from shipping_request import ShippingRequest
from standard_shipping import StandardShipping
from express_shipping import ExpressShipping
from free_shipping import FreeShipping
from order_service import OrderService


class Application:
    def handle_request(self, shipping_type, weight, distance, order_total):

        try:
            shipping_request = ShippingRequest(weight, distance, order_total)
        except ValueError as e:
            return f"error: {e}"

        if shipping_type == "standard":
            strategy = StandardShipping()
        elif shipping_type == "express":
            strategy = ExpressShipping()
        elif shipping_type == "free":
            strategy = FreeShipping()
        else:
            raise ValueError("Invalid shipping type")

        order_service = OrderService(strategy)

        result = order_service.calculate_shipping(shipping_request)

        return result