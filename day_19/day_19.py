file = open("example.txt", "w")
file.write("Hello Ahmad, welcome to file handling!")
file.close()
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
file = open("example.txt", "a")
file.write("\nThis is a new line added.")
file.close()
file = open("example.txt", "r")

for line in file:
    print(line)

file.close()
with open("example.txt", "r") as file:
    print(file.read())
    names = ["Ahmad", "Aliyu", "John", "Mary"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
        