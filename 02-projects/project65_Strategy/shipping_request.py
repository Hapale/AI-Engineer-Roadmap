class ShippingRequest:

    def __init__(self, weight: float, distance: float, order_total: float):

        if weight <= 0 :
            raise ValueError ("Weight can't small than zero")
        if distance <= 0:
            raise ValueError ("Distance most posetive")
        if order_total < 0:
            raise ValueError ("Total order most posetive")

        self.weight = weight
        self.distance = distance
        self.order_total = order_total