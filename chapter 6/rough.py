"""getter and setter """
class MyClass:
    # def __init__(self,value):
    #     self._value = value
    def __init__(self):
        self._value = 0
    def show(self):
        print(f"Value is {self._value}")
    @property
    def multiple(self):
        return 2*self._value
    @multiple.setter
    def multiple(self,new_value):
        self._value = new_value/10


obj = MyClass()
obj.multiple = 15
print(obj.multiple)
obj.show()
