class ShippingResult:

    def __init__(self, cost: float):

        if cost < 0 :
            raise ValueError ("Cost can't small than zero")
        
        self.cost = cost

    def __str__(self):

        return (f"Cost:{self.cost}\n")