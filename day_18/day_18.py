def decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


@decorator
def greet():
    print("Hello Ahmad")

greet()
def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return func(a, b)
    return wrapper


@smart_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(a, b):
    return a + b

print(add(5, 7))
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end - start)
    return wrapper


@timer
def slow_function():
    time.sleep(2)
    print("Finished slow function")

slow_function()