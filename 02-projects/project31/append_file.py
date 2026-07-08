print("===== Append File =====")
print()

file = open("students.txt", "a")

file.write("\nMohammad")

file.close()

print("Student added.")