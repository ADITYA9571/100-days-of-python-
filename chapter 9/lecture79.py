# method resolution order 
class Employee:
    def __init__(self, name):
        self.name = name 
    def show(self):
        print(f"The name is {self.name}")
class Dancer:
    def __init__(self, Dance):
        self.Dance = Dance 
    def show(self):
        print(f"The Dance is {self.Dance}")
class DancerEmpoyee(Dancer, Employee):
    def __init__(self, name, Dance):
        self.Dance = Dance
        self.name = name

obj1 = DancerEmpoyee("Sivani","kathak")
print(obj1.name)
print(obj1.Dance)
obj1.show()
print(DancerEmpoyee.mro())
# Memory resolution order 
# [<class '__main__.DancerEmpoyee'>, <class '__main__.Employee'>, <class '__main__.Dancer'>, <class 'object'>]
# [<class '__main__.DancerEmpoyee'>, <class '__main__.Dancer'>, <class '__main__.Employee'>, <class 'object'>]
# [<class '__main__.DancerEmpoyee'>, <class '__main__.Dancer'>, <class '__main__.Employee'>, <class 'object'>]