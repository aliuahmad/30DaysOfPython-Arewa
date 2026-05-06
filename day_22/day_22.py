class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "is speaking")


class Student(Person):
    pass


s1 = Student("Ahmad")
s1.speak()
class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "is speaking")


class Student(Person):
    def study(self):
        print(self.name, "is studying")


s1 = Student("Ahmad")
s1.speak()
s1.study()
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark bark")


a = Animal()
d = Dog()

a.sound()
d.sound()
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


s1 = Student("Ahmad", "A")
print(s1.name)
print(s1.grade)