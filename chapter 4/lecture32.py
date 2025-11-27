"""
s1 = {1,2,4,5,7,8}
s2 = {3,6}
print(s1,s2)
print("s1 union s2",s1.union(s2))
s1.update(s2)
print(s1,s2)
"""
cities1 = {"c1","c2","c3"}
cities2 = {"c1","c2","c3","c4","c5"}
print("intersection ",cities1.intersection(cities2))
cities3 = cities1.intersection(cities2)
print(cities3)
cities4 = cities1.symmetric_difference(cities2)
print(cities4)
cities5 = cities1.difference(cities2)
print(cities5)
cities6 = cities1.isdisjoint(cities2)
print(cities6)
cities7 = cities1.issubset(cities2)
print(cities7)
cities8 = cities2.issuperset(cities1)
print(cities8)
print("We can try add, update, remove, discard, pop, del set, check if item ")