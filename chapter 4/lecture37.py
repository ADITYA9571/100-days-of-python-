"""Use of finally eyword"""
print("basically finally keyword is used in function call to run a block each time weither try or catch block")
print("for example in case of revoking data in DBMS")

def func1():
    """sample of try except and finally block"""
    try:
        l = [1,3,5,7,9]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except Exception as e :
        print("Some eroor occured:- ",e)
        return 0

    finally:
        print("ALWAYS EXECUTED")

x = func1()
print(x)
