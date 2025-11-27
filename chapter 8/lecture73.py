"""Dunder methods"""
# they are defined in the class for some specific work purpose 
# __init__
# __str__
# __repr__
# __call__
class check :
    def __init__(self, name):
        self.name = name 
        print("wow")
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return f"Employee name is {self.name} through str"
    def __repr__(self):
        return f"Employee {self.name} through repr "
    def __call__(self):
        print(f"Heyy!! {self.name}")
