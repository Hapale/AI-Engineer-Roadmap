class Student:
    def __init__(self, name):

        self.name = name
    
    def passed(self, score):

        return score >= 50
    
student = Student("Ali")

print(student.passed(80))

print(student.passed(30))

