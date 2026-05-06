class Person:
    pass
p1 = Person()
print(p1)
p1 = Person()
print(p1)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Ahmad", 30)

print(p1.name)
print(p1.age)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Ahmad", 30)
p1.greet()
p1 = Person("Ahmad", 30)
p2 = Person("Aisha", 25)

p1.greet()
p2.greet()
class Student:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

s1 = Student("Ali")
s2 = Student("Fatima", 95)

print(s1.score)
print(s2.score)
s1.score = 80
print(s1.score)
del s1.score
del s1
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Bingo", "German Shepherd")
dog2 = Dog("Max", "Labrador")

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawn:", amount)


acc1 = BankAccount("Ahmad", 1000)

acc1.deposit(500)
acc1.withdraw(200)

print("Final balance:", acc1.balance)
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount
        print("New price:", self.price)


lap1 = Laptop("HP", 300000)
lap1.apply_discount(10)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rec = Rectangle(5, 3)

print("Area:", rec.area())
print("Perimeter:", rec.perimeter())
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print("Login successful")
        else:
            print("Invalid credentials")

user1 = User("admin", "1234")

user1.login("admin", "1234")
user1.login("admin", "1111")