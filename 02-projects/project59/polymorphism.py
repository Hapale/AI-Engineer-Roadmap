class Dog:

    def sound(self):

        print("Woof")


class Cat:

    def sound(self):

        print("Meow")


class Bird:

    def sound(self):

        print("Tweet")


animals = [Dog(), Cat(), Bird()]

for animal in animals:

    animal.sound()