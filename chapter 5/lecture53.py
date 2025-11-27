"""maps and filter are higher order function: those wwho takes inout as a function"""
# def cube(x):
#     """definition of cube"""
#     return x*x*x
# print(cube(2))
l = [1,2,3,4,5]
#--mapping()
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)
# newl = list(map(cube,l)) // newl = list(map(lambda x: x*x*x,l))
# print(newl)
#--filtering()
# def filter_func(a):
#     """filter function"""
#     return a<5
# newl = list(filter(filter_func,l)) // newl = list(filter(lambda x:x<5,l))
# print(newl)
from functools import reduce
sum = reduce(lambda x,y:x + y, l)
print(sum)          
