class Car:
    
    def __init__(self, brand):

        self.brand = brand

    def drive(self, speed):

        print(self.brand, "is driving at", speed, "km/h")


car = Car("BMW")

car.drive(150)