class Car:
    def __init__(self, brand, color):

        self.brand = brand

        self.color = color

    def show(self):

        print(self.brand, "-", self.color)


car1 = Car("BMW", "Black")
car2 = Car("Toyota", "White")
car3 = Car("Ford", "Blue")

car1.show()
car2.show()
car3.show()
