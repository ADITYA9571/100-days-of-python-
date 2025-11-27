marks = [4,5,1,"7","aditya","mark"]
"""
print(marks)
print(type(marks))
print(marks[2])
print(marks[-2])
print(marks[len(marks)-2])
print(marks[6-2])
print(marks[4])
if 5 in marks:
    print("yes")
else:
    print("no")
if "7" in marks:
    print("yes")
else:
    print("no")
if "5" in marks:
    print("yes")
else:
    print("no")
if 7 in marks:
    print("yes")
else:
    print("no")
if "adit" in "aditya":
    print("yes")
else:
    print("no")

print(marks)
print("by default it choses 0 as start and len(array) as end and jump as 1")
print("starting to previos of end")
print(marks[1:-1])
print("starting ending jump") 
print(marks[1:5:2])

"""
print("list compehension:")
lst = [i*i for i in range(10)]
print (lst)

lst2 = [i*i for i in range(10) if i%2==1]
print (lst2)