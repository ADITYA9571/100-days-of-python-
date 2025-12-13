# 1
print("Aditya Mohan Jha")
# 2
num1 = int(input("number1:"))
num2 = int(input("number2:"))
print("Sum",num1+num2)
# 3
num1 = int(input("number1:"))
num2 = int(input("number2:"))
temp = num1
num1 = num2 
num2 = temp 
print(f"Num1{num1}Num2{num2}")
# 4
num1 = int(input("number1:"))
print(f"Square= {num1**2}, Cube= {num1**3}")
# 5
char1 = str(input("char:"))
print(ord(char1))
# 6
cel = float(input("Enter celcius value :"))
print(f"Fahrenheit = {cel * 9 / 5 + 32}")
# 7
amount = int(input("Enter amount: "))
time = int(input("Enter time: "))
interest = int(input("Enter interest: "))
print(f"simple interset  = {amount*interest*time}")
# 8
num1 = int(input("number1:"))
if num1 < 0:
    print("negative")
elif num1 > 0:
    print("positive")
else :
    print("zero")
# 9
num1 = int(input("number1:"))
num2 = int(input("number2:"))
num3 = int(input("number3:"))
print(max(num1, num2, num3))
# 10
num1 = int(input("number1:"))
if num1%2 == 0:
    print("Even")
else :
    print("zero")
# 11
year = int(input("year1:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else :
    print("Not leap year")
# 12
radius = int(input("radius1:"))
print(f"area{2 * 3.14 * radius}")
# 13
Kilometer = int(input("Kilometer1:"))
print(f"miles{ 0.621 * Kilometer}")
# 14
user_input = str(input("user_input:"))
num1 = ord(char1)
if (num1 >= 65 and num1 <=122):
    print("Alphabet")
elif(num1 >= 48 and num1 <=57):
    print("interger")
else:
    print("Not found ")
# 15
number = int(input("number1:"))
reversed_num = 0
while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number = number // 10 
print(reversed_num)
# 16
number = int(input("number1:"))
divisor = int(input("divisor1:"))
number2 = number//divisor
reminder = number - (number2*divisor)
print(reminder)
# 17 
char1 = input("Enter your character:")
if (char1 == "a" or char1 == "e" or char1 == "i" or char1 == "o" or char1 == "u"):
    print("Vowel")
elif(char1 == "A" or char1 == "E" or char1 == "I" or char1 == "O" or char1 == "U"):
    print("Vowel")
else:
    print("consonants")
# 18
for i in range ( 1, 11):
    print(f"Natural number:{i}")
# 19
minutes = int(input("Enter mintes"))
hours = int(minutes / 60)
minutes = minutes - (hours * 60) 
print(f"Hours{hours}:Minues{minutes}")
# 20
amount = int(input("Enter amount: "))
time = int(input("Enter time: "))
interest = int(input("Enter interest: "))
print(f"compund interset  = {amount*((1+interest)**time)}")