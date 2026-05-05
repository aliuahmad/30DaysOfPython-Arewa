class Person:
    pass

print(Person)
p = Person()
print(p)
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

p1 = Person("Ahmad", "Aliyu", 30)
print(p1.firstname)
print(p1.lastname)
print(p1.age)
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def full_name(self):
        return self.firstname + " " + self.lastname

p1 = Person("Ahmad", "Aliyu", 30)
print(p1.full_name())
p1.age = 31
print(p1.age)
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def full_name(self):
        return self.firstname + " " + self.lastname

    def introduce(self):
        return f"My name is {self.full_name()} and I am {self.age} years old"

p1 = Person("Ahmad", "Aliyu", 30)
print(p1.introduce())