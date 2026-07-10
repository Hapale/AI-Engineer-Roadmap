class Person:

    def __init__(self, name):

        self.name = name

        print("Person created")

class Student(Person):

    def __init__(self, name):


        print("Student created")


student = Student("Ali")