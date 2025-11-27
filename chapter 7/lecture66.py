class Employee:
    company_name = "Apple"   #class variable 
    no_of_Employees = 0
    def __init__ (self,name):
        self.name = name
        self.raise_Amount = 0.02   #instance variable
        Employee.no_of_Employees += 1
    def showDetails (self):
        print(f"Name {self.name}, raised amount in {self.no_of_Employees} sized {self.company_name} is {self.raise_Amount}")

emp1 = Employee("Aditya")
emp1.showDetails()
emp2 = Employee("Chetan")
emp2.raise_Amount = 0.03
emp2.company_name = "Google"
emp2.showDetails()
