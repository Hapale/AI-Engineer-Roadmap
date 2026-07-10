class Car:

    def __init__(self, brand):

        self.brand = brand

    def start(self):
        
        print(self.brand, "started")

car = Car("BMW")

car.start()