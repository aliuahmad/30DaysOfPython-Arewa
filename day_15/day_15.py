try:
    print(10 / 0)
except:
    print("You cannot divide by zero")


name = "Alice"
try:
    print(name)
except NameError:
    print("Variable is not defined")


try:
    num = 10 / 2
except:
    print("Error occurred")
else:
    print("Result:", num)


try:
    print(5 + "5")
except TypeError:
    print("Type mismatch error")
finally:
    print("Execution completed")


age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input")