class Person:

    def __init__(self, name):
        
        self.name = name

class Student(Person):

    pass

student = Student("Ali")

print(student.name)