import random
my_set = {"snake","water","gun"}
print("snake water gun")
print("computer:******")
choice = str(input("Enter choice:"))
random_item = random.choice(list(my_set))
# print(random_item)
dict1 = {'snake':0,'water':1,'gun':2}
print("computer:"+random_item)
matrix = [
    ["DRAW","WIN","LOSE"],
    ["LOSE","DRAW","WIN"],
    ["WIN","LOSE","DRAW"]
]
print(matrix[dict1[choice]][dict1[random_item]])
