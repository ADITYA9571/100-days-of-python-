"""Access MOdifieres in python, by default public"""
# name mangling 
# basic inheritence does PUBLIC access modifier by default 
# //for private 
# class employee:
#     def __init__(self):
#         self.__name ="Aditya "
# a = employee()
# print(a._employee__name)
# //for protected
# /--protected by convenience (_name)
# class employee:
#     def __init__(self):
#         self._name ="Aditya "
# a = employee()
# print(a._name)
class student:
    def __init__(self):
        self._name = "Harry"
    def _funName (self): #protected method 
        return "CODE WITH HARRY"

class subject(student):
    pass
obj = student()
obj1 = subject()
print(dir(obj))
print(obj._name)
print(obj._funName())
print(obj1._name)
print(obj1._funName())