"""Inheritence """
class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id

    def showdetails(self):
        print(f"Employee {self.id} is {self.name}")

class implicit(Employee):
    """Child class"""
    def about(self):
        print("He is in AI/ML domain")

e1 = Employee("Aditya",1565)
e1.showdetails()
e2 = implicit("Unknown", 1334)
e2.showdetails()
e2.about()
