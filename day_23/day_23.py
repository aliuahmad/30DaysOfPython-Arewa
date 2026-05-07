# Exercise 1 — Student Grades
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def display_info(self):
        print("Name:", self.__name)
        print("Grade:", self.__grade)


s1 = Student("Ahmad", 85)
s1.display_info()
s1.set_grade(95)
print("Updated Grade:", s1.get_grade())


print("------------")


# Exercise 2 — Temperature Converter
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def set_temp(self, temp):
        self.__celsius = temp

    def get_temp(self):
        return self.__celsius

    def to_fahrenheit(self):
        return (self.__celsius * 9/5) + 32


t1 = Temperature(30)
print("Celsius:", t1.get_temp())
print("Fahrenheit:", t1.to_fahrenheit())


print("------------")


# Exercise 3 — Secure Login
class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def login(self, username, password):
        if username == self.__username and password == self.__password:
            print("Access granted")
        else:
            print("Access denied")


u1 = User("admin", "1234")
u1.login("admin", "1234")
u1.login("admin", "0000")