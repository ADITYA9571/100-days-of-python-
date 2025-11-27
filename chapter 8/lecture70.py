"""obj1.split("-")"""
class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],string.split("-")[1])
e1=Employee("Harry",2000)
print(e1.name)
print(e1.salary)
stringinput = "Aditya-2500"
e2=Employee.fromStr(stringinput)
print(e2.name)
print(e2.salary)

class person_ck:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def fromStr(cls, string):
        name, age = (string.split(","))
        return cls(name,int(age))

person = person_ck.fromStr("Aditya Jha, 21")
print(person.name, person.age)    
 