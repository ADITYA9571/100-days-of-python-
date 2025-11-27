"""This script demonstrates basic dictionary operations in Python."""
dict1 = {'name':'aditya','age':21,'status':'single'}
print(dict1)
print("Error output type dict-",dict1['name'])
print("None output:",dict1.get('name'))
print(dict1.keys())
print(dict1.values())

#for key in dict1.keys():
#    print("Key:",dict1.keys(),"Values:",dict1.values())
#    print(f"Key: {dict1.keys()} Values: {dict1.values()}")
#    print(f"Key: {key} Values: {dict1[key]}")

print(dict1.items())
for key, value in dict1.items():
    print(f"key : {key} X values : {value}")
