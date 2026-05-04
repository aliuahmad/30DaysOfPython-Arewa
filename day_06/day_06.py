# DAY 06 — STRINGS

# 1 & 2 Concatenation
print(" ".join(["Thirty", "Days", "Of", "Python"]))
print(" ".join(["Coding", "For", "All"]))

# 3–4 Variable
company = "Coding For All"
print(company)

# 5 Length
print(len(company))

# 6 Upper / 7 Lower
print(company.upper())
print(company.lower())

# 8 Formatting methods
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Slice "Coding"
print(company[0:6])

# 10 Contains "Coding"
print("Coding" in company)

# 11 Replace Coding → Python
print(company.replace("Coding", "Python"))

# 12 Python for Everyone → Python for All
phrase = "Python for Everyone"
print(phrase.replace("Everyone", "All"))

# 13 Split company
print(company.split())

# 14 Split tech companies
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(", "))

# 15 Character at index 0
print(company[0])

# 16 Last index
print(len(company) - 1)

# 17 Character at index 10
print(company[10])

# 18 Acronyms
pfe = "Python For Everyone"
cfa = "Coding For All"
print("".join([word[0] for word in pfe.split()]))
print("".join([word[0] for word in cfa.split()]))

# 19 First occurrence of C
print(company.find("C"))

# 20 Position of F
print(company.find("F"))

# 21 Last occurrence of l
sentence = "Coding For All People"
print(sentence.rfind("l"))

# 22–24 because sentence
because_sentence = "You cannot end a sentence with because because because is a conjunction"
print(because_sentence.find("because"))
print(because_sentence.rfind("because"))

start = because_sentence.find("because")
end = because_sentence.rfind("because") + len("because")
print(because_sentence[start:end])

# 25 Startswith
print(company.startswith("Coding"))

# 26 Endswith
print(company.endswith("coding"))

# 27 Remove spaces
messy = "   Coding For All      "
print(messy.strip())

# 28 Identifier check
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 29 Join with #
frameworks = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#".join(frameworks))

# 30 New line escape
print("I am enjoying this challenge.\nI just wonder what is next.")

# 31 Tab escape
print("Name\tAge\tCountry\tCity")
print("Ahmad\t30\tNigeria\tAbuja")

# 32 Area of circle
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 33 Arithmetic formatting
a, b = 8, 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")