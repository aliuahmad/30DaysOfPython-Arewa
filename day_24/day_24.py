def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

print(next(g))
print(next(g))
print(next(g))
def count_up_to(n):
    for i in range(1, n + 1):
        yield i
squares = (x * x for x in range(6))

for s in squares:
    print(s)
def even_numbers():
    for i in range(2, 21, 2):
        yield i


for num in even_numbers():
    print(num)