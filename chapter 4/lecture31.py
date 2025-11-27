print("Sets doesnt prints in order,andskips the repeated values")
set1 = {}
print(type(set1),"Empty dictionary")
set2 = ()
print(type(set2),"Empty tuple")
set3 = set()
print(type(set3),"Empty set")

s = set()
s.add("apple")
s.add("banana")
s.add("cherry")

print("Printing set elements in insertion order:")
for item in s:
    print(item)
