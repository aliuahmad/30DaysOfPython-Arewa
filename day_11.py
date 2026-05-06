def full_name(first_name, last_name):
    return first_name + " " + last_name

print(full_name("Ahmad", "Aliyu"))
def add_two_numbers(a, b):
    return a + b

print(add_two_numbers(5, 7))
def area_of_circle(radius):
    pi = 3.14
    return pi * radius * radius

print(area_of_circle(5))
def is_even(num):
    return num % 2 == 0

print(is_even(4))
print(is_even(7))
def count_items(lst):
    return len(lst)

print(count_items([1,2,3,4,5]))
def find_max(a, b, c):
    return max(a, b, c)

print(find_max(3, 10, 6))
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(30))def check_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Autumn"

print(check_season("July"))