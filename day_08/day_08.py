empty_tuple = ()
print(empty_tuple)
brothers = ("Suleiman", "Ibrahim")
sisters = ("Khadijah", "Maryam", "Munira")
siblings = brothers + sisters
print(siblings)
print(len(siblings))
family_members = siblings + ("Father", "Mother")
print(family_members)
brother1, brother2, sister1, sister2, sister3 = siblings
print(brother1)
print(sister1)
print(siblings[1:3])
print("Khadijah" in siblings)
siblings_list = list(siblings)
print(siblings_list)
del siblings
empty_tuple = ()

brothers = ("Suleiman", "Ibrahim")
sisters = ("Khadijah", "Maryam", "Munira")

siblings = brothers + sisters
print(siblings)

print(len(siblings))

family_members = siblings + ("Father", "Mother")
print(family_members)

# unpacking
b1, b2, s1, s2, s3 = siblings
print(b1, s1)

print(siblings[1:3])

print("Ibrahim" in siblings)

siblings_list = list(siblings)
print(siblings_list)

del siblings