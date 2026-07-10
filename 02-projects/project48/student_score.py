class Student:

    def __init__(self, name):

        self.name = name

    def show_score(self, score):

        print(self.name, "scored", score)

student = Student("Ali")

student.show_score(95)