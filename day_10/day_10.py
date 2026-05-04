empty_dict = {}
print(empty_dict)
person = {
    "first_name": "Ahmad",
    "last_name": "Aliyu",
    "age": 30,
    "country": "Nigeria",
    "skills": ["Python", "Git", "Data Analysis"]
}

print(person)
print(person["first_name"])
print(person.get("age"))
person["city"] = "Abuja"
print(person)
person["age"] = 31
print(person)
print("skills" in person)
print(person.keys())
print(person.items())
person.pop("city")
print(person)