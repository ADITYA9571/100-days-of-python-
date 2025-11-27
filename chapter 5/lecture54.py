"""We are gonna check 'is' and '==' comparision"""
# is compares the exact location of memory
# == compares the value 
# immutable are always true 
print("'is ' '=='")
a=5
b=5
print(a is b, a == b,"a,b")
c="aditya"
d="aditya"
print(c is d, c == d,"c,d")
e=(1,2,3,4)
f=(1,2,3,4)
print(e is f, e == f,"e,f in tuple")
g={1,2,3,4}
h={1,2,3,4}
print(g is h, g == h,"g,h in set")
i=[1,2,3,4]
j=[1,2,3,4]
print(i is j, i == j,"i,j in list")
k=None
l=None
print(k is l, k == l,"k,l")
m=7
n="7"
print(m is n, m == n,"m,n")
dict1 = {'name1':'aditya','name2':'mohan','name3':'jha'}
dict2 = {'name1':'aditya','name2':'mohan','name3':'jha'}
print(dict1 is dict2, dict1 == dict2,"dict1 and dict2")