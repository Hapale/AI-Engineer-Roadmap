print("===== Name Saver =====")

name = input("Enter your name: ")

file = open("names.txt", "a")

file.write(name + "\n")

file.close()

print("Name saved successfully.")