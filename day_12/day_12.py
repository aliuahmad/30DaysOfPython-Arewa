# day_12.py

import my_module

print(my_module.generate_full_name("Ahmad", "Aliyu"))
print(my_module.sum_two_nums(10, 20))
print(my_module.person_info("Ahmad", "Aliyu", "Nigeria", 31))
print(my_module.add_all_nums(1, 2, 3, 4, 5))
from my_module import generate_full_name, sum_two_nums

print(generate_full_name("John", "Doe"))
print(sum_two_nums(5, 6))
import math
import random

print("Square root of 25:", math.sqrt(25))
print("Random number:", random.randint(1, 10))