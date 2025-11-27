print("Factorial Code:")

def factorial(num):
    if num == 1 :
        return 1
    return num * factorial(num - 1)

print("Enter number:")
num = int(input("num="))
result = factorial(num)
print(f"Factorial of {num} is {result}")
