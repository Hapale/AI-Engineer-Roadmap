class Student:
    def __init__(self, name):
        
        self.name = name

    def introduce(self):

        print("Hello, I am", self.name)

student = Student("Ali")

student.introduce()