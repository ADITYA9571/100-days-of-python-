print("switch-case in python is match-case")
x = int(input("Enter the value of x="))
match x:
    case 0:
        print("value is zero")
    case _ if x%2==0:
        print("Value is even")
    case _:
        print("Value is odd")
