"""dir(), __dict__(), help"""
x= [1,2,3]
print(dir(x))
print(x.__reversed__)
class Person:
    def __init__(self,name, age):
        self.name = name 
        self.age = age

p = Person("John",30)
print(p.__dict__) # shows attribute passes in the class as a dictionary 
print(help(Person)) #used to get documentaion of an object 
