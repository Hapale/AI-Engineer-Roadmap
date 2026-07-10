class Car:

    def start(self):

        self.check_engine()

        self.check_fuel()

        self.turn_on()

    def check_engine(self):

        print("Engine OK")

    def check_fuel(self):

        print("Fuel OK")

    def turn_on(self):

        print("Car Started")

car = Car()

car.start()