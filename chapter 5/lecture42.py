"""Enumerate function in python"""
fruits = ["Apple","Banana","Cherry","Guava"]
index1 = 0
for item in fruits:
    print(item)
    if index1==2 :
        print("Red colour")
    index1 = index1+1

marks = [11,12,13,14,15,16,17,18,19,20]
for index,result in enumerate(marks,start=3):
    print(result)
    if index==3 :
        print("WOOW!!")
