numbers = [i for i in range(1, 11)]
print(numbers)
squares = [i * i for i in range(1, 11)]
print(squares)
evens = [i for i in range(1, 21) if i % 2 == 0]
print(evens)
odds = [i for i in range(1, 21) if i % 2 != 0]
print(odds)
words = ["python", "java", "javascript"]
upper_words = [word.upper() for word in words]
print(upper_words)
words = ["apple", "banana", "cherry"]
lengths = [len(word) for word in words]
print(lengths)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)
words = ["cat", "dog", "apple", "banana", "fish"]
filtered = [word for word in words if "a" in word]
print(filtered)