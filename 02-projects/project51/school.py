class Student:

    school = "AI Academy"

    def __init__(self, name):

        self.name = name

student1 = Student("Ali")
student2 = Student("Sara")

print(student1.school)
print(student2.school)

print(student1.name)
print(student2.name)