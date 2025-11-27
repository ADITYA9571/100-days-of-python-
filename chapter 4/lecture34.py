"""dictionary methods in python """
ep1 = {100:45,101:67,102:69,103:99}
ep2 = {104:32,105:65}
ep1.update(ep2)
print(ep1)
ep1.pop(101)
print(ep1)
ep1.popitem()
print(ep1)
ep1.clear()
print(ep1)
ep3 = {}
print(ep3)
# del ep1[122]
# del ep1
