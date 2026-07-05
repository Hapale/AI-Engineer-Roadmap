print("===== Student Manager =====")

students = ["Ali", "Sara"]

print("Initial list:")
print(students)

students.append("Reza")

print("\nAfter adding Reza:")
print(students)

students[0] = "Amir"

print("\nAfter changing first student:")
print(students)

students.remove("Sara")

print("\nAfter remove Sara:")
print(students)

print("\nTotal students:")
print(len(students))
