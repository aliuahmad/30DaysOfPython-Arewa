empty_set = set()
print(empty_set)
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(it_companies)
print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Tesla", "Meta", "OpenAI"])
print(it_companies)
it_companies.remove("Apple")
print(it_companies)
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))