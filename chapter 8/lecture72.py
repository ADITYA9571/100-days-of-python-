"""Super Keyword"""
# use to refer the parent class 
# class parentclass:
#     def parentmethod(self):
#         print("this is parent class")
# class childclass(parentclass):
#     def parentmethod(self):
#         print("Here parent is Aditya")
#         super().parentmethod()
#     def childmethod(self):
#         print("this is child class")
#         print("calling parent through child class")
#         super().parentmethod()

# child1 = childclass()
# child1.childmethod()
# child1.parentmethod()

class Employee:
    def __init__(self, name ,ID):
        self.name = name 
        self.ID = ID

class Programmer (Employee):
    def __init__(self,name , ID , language):
        super().__init__(name ,ID)
        self.language = language
    
Emp1 = Employee("Aditya",2002)
Pro1 = Programmer("Chetan",2000,"Java")
print(Emp1.ID)
print(Pro1.ID)
