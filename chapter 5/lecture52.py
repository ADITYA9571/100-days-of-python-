"""lambda function"""
def sum(x,y):
    return x+y
def apple(fx,value):
    return 6 + fx(value)
double = lambda x: x*2
square = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y,z: x+y+z

print(double(5))
print(avg(2,3,4))
print(apple(square,6))
print(apple(cube,6))
print(apple(lambda x:x*x*x,6))
