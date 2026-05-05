numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x * x, numbers))
print(squared)
words = ["python", "java", "javascript"]

upper = list(map(str.upper, words))
print(upper)
numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
words = ["apple", "banana", "cat", "elephant", "dog"]

long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)
print(total)
numbers = [10, 5, 8, 20, 3]

maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)