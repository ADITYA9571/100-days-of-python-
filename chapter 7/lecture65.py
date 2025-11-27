# static methods
# no need to add self argument in static method 
def add(a,b):
    return a+b
class Method:
    def __init__(self,num):
        self.num = num 
    def addtonum(self, n):
        self.num = self.num + n
    @staticmethod #decorater
    def add(a,b):
        return a+b

result = Method.add(3,4)
print(f"type 1-{result}")
obj1 = Method(5)
print(f"type 2-{obj1.num}")
print(f"type 3-{obj1.addtonum(6)}")
print(f"type 4-{Method.add(6,7)}")
print(f"type 5-{add(9,10)}")
