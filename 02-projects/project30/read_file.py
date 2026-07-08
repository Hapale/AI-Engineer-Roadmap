print("====== Read File ======")

file = open("message.txt", "r")

text = file.read()

print(text)

file.close()