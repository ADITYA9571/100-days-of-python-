"""huef"""
import random
my_string = "abcdefghijklmnoprstuvwxyz0123456789"
# random_char = random.choice(my_string)

def encode(string1):
    """Function for encode"""
    if len(string1) < 3:
        print(string1[::-1])
    else:
        print(
            f"{random.choice(my_string)}{random.choice(my_string)}{random.choice(my_string)}"
            f"{string1[1:]}{string1[0]}"
            f"{random.choice(my_string)}{random.choice(my_string)}{random.choice(my_string)}"
        )

def decode(string1):
    """Function for decode"""
    if len(string1) < 3:
        print(string1[::-1])
    else:
        print(string1[-4]+string1[3:-4])

choice = int(input("Do you want to encode(1) or decode(2):-"))
if choice == 1:
    print("Enter string for encode:")
    string2= input()
    encode(string2)
else:
    print("Enter string for encode:")
    string2= input()
    decode(string2)
