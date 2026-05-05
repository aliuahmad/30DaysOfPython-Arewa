class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def full_name(self):
        return self.firstname + " " + self.lastname
class Student(Person):
    pass

s1 = Student("Ahmad", "Aliyu")
print(s1.full_name())
class Student(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname)
        self.age = age

s1 = Student("Ahmad", "Aliyu", 30)
print(s1.full_name())
print(s1.age)
class Student(Person):
    def __init__(self, firstname, lastname, age):
        super().__init__(firstname, lastname)
        self.age = age

    def introduce(self):
        return f"I am {self.full_name()} and I am {self.age} years old"

s1 = Student("Ahmad", "Aliyu", 30)
print(s1.introduce())
class Student(Person):
    def full_name(self):
        return f"Student: {self.firstname} {self.lastname}"

s1 = Student("Ahmad", "Aliyu")
print(s1.full_name())

