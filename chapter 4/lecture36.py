"""Exception handling in python"""
# a = input("Enter number:")
# print(f"multiplication table of {a} is:-")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {int(i)} = {int(a*i)}")
# except Exception as e:
#     print("Invalid Input")
# print("End of progeam ")
try:
    num = int(input("Enter number "))
    a =[6,3]
    print(a[num])
except ValueError:
    print("Invalid error")
except IndexError:
    print("Index error")
