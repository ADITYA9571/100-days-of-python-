l = [1,5,9,32,"aditya",9]
j = [8,2,9,1,5,7,0,6,3,4]
print(type(l),l)
l.append(93)
print(l)
j.sort()
print(j)
j.sort(reverse=True)
print(j)
l.reverse()
print(l)
print(l.index(9))
print("l.index(8) = ValueError: 8 is not in list")
print(l.count(9))
m=l
print("m=l just makes the reference of the lists")
m[0]=22
print("list m is",m)
print("list l is",l)
m=l.copy()
print(m)
print(l)
m[0]=3
print(m)
l.insert(0,7)
print(l)
k=[900,1000,1100]
a = k+m
print("concatenated",a)
l.extend(k)
print(l)