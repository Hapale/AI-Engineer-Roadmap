class Student:
    def __init__(self, name, age):
        
        self.name = name
        self.age = age

    def introduce(self):
        
        print("Name", self.name)

        print("Age", self.age)
        
student1 = Student("Ali", 20)
student2 = Student("Sara", 22)

student1.introduce()
student2.introduce()
