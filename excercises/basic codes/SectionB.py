# 1
number1 = int(input("enter the number:"))
print("TABLE")
for i in range(1, 11):
    print(f"{number1} X {i} = {number1*i}")
# 2
for i in range(1,101):
    if(i%2==0):
        print(f"Even {i}")
# 3
number1 = int(input("enter the number:"))
print("SUM = ", number1*(number1+1)/2)
# 4
number1 = int(input("enter the number:"))
fact = 1
for i in range(1, number1+1):
    fact = i*fact
print("Factorial = ",fact)
# 5
number1 = int(input("enter the number:"))
count = 0
while number1 > 0:
    number1 = number1 // 10 
    count = count + 1
print("countorial = ",count)
# 6
number1 = int(input("enter the number:"))
temp = number1
reversed_num = 0
while number1 > 0:
    digit = number1 % 10
    reversed_num = reversed_num * 10 + digit
    number1 = number1 // 10 
if temp == reversed_num:
    print("Palindrome")
else:
    print("NOt palindrome")
# 7 
num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0
n = len(str(num))
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** n
    num //= 10
if sum_of_powers == temp:
    print(f"{temp} is an Armstrong number.")
else:
    print(f"{temp} is not an Armstrong number.")
# 8
number = int(input("Enter number upto:"))
num1 = 0
temp = 0
num2 = 1
print(num1)
print(num2)
for i in range (3, number + 1):
    temp = num1+num2 
    num1 = num2
    num2 = temp
    print(temp)
# 9
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
GCD = 0
for i in range (1, max(number1, number2)):
    if (number2%i==0 and number1%i==0):
        GCD = i
if(GCD == 0):
    print("no common divisor")
else:
    print("GCD=", GCD)
# 10
number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))
GCD = 0
for i in range (1, max(number1, number2)):
    if (number2%i==0 and number1%i==0):
        GCD = i
LCM = number1*number2/GCD
print("LCM", LCM)
# 11
print("2")
print("3")
for i in range(4,101):
    j = 1
    flag = 0
    while(j <= i/2):
        j = j+1
        if i%j == 0:
            flag = 1
    if(flag != 1):
        print(i)
# 12
num1 = int(input("Enter the lowest"))
num2 = int(input("Enter the highest"))
count = 0
for i in range(num1,num2+1):
    j = 1
    flag = 0
    while(j <= i/2):
        j = j+1
        if i%j == 0:
            flag = 1
    if(flag != 1):
        count = count + 1
print(count)
# 13
number1 = int(input("Enter the number"))
sum1 = 0
sum2 = 0
while number1 > 0:
    digit = number1 % 10
    if(digit%2==0):
        sum1 = sum1+digit
    else:
        sum2 = sum2+digit
    number1 = number1 // 10 
print(f"sum of even{sum1} sum of odd{sum2}")
# 14
number1 = int(input("Enter the number"))
sum1 = 0
for i in range(1,(int(number1/2)) + 1):
    if(number1%i==0):
        sum1 = sum1 + i
if(sum1 == number1):
    print(f"perfect number{sum1}")
else:
    print("not perfedt")
# 15
print("Print pattern")
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end = "")
    print(" ")
# 16
print("Print pattern")
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*", end = "")
    print(" ")
# 17
print("Print Pyramid:")
for i in range(1,6):
    j = i
    while ( 4 - j >= 0):
        print(" ", end = "")
        j = j + 1
    j = i
    while (j > 0):
        print(i, end = " ")
        j = j - 1 
    print("")
# 18
num1 = int(input("Enter the number:"))
for i in range(1,int(num1/2)+1):
    if(num1%i==0):
        print(i)
# 19
number1 = int(input("Enter the number"))
count = 0
while number1 > 0:
    digit = number1 % 10
    if(digit%3==0):
        count = count+1
    number1 = number1 // 10 
print(f"counts{count}")
# 20
number1 = int(input("Enter the number"))
sum1 = 0
for i in range(1, number1+1):
    sum1 = i**2 + sum1
print(sum1)
