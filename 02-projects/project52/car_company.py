class Car:

    wheels = 4

    def __init__(self, brand):

        self.brand = brand

car1 = Car("BMW")
car2 = Car("Toyota")

print(car1.wheels)
print(car2.wheels)

print(car1.brand)
print(car2.brand)