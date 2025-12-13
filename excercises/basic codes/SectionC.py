# enumerate,
# 1. Count number of vowels in a string.
string1 = str(input("Enter the string:"))
vowels = "AEIOUaeiou"
count = 0
for i in range(0, len(string1)-1):
    if string1[i] in vowels:
        count = count + 1
print("total number of voweks: ", count)

# 2. Reverse a string without using slicing.
string1 = str(input("Enter the string:"))
string1 = "".join(reversed(string1))
print(string1)

# 3. Check if a string is palindrome.
string1 = str(input("Enter the string:"))
string2 = ""
for i in range(len(string1)-1, -1, -1):
    string2 = string2 + string1[i]
if(string2 == string1):
    print("palindrome ")
else:
    print("NOt palindrome")

# 4. Count frequency of each character in a string.
string1 = str(input("Enter the string:"))
store = ""
count = 0
for i, char1 in enumerate(string1):
    if char1 not in store:
        store = store + string1[i]
for i,char1 in enumerate(store):
    count = 0
    for j,char2 in enumerate(string1):
        if(char1==char2):
            count = count + 1
    print(f"total number of {char1} is: ", count)

# 5. Convert string to uppercase without using built-in function.
string1 = str(input("Enter the string:"))
string2 = ""
for i, char1 in enumerate(string1):
    if (ord(char1) > 96 and ord(char1) < 122):
        temp = ord(char1) - 32
        string2=string2 +chr(temp)
    else:
        string2 = string2 + char1
print(string2)

# 6. Remove all spaces from a string.
string1 = str(input("Enter the string:"))
string2 = ""
for i, char1 in enumerate(string1):
    if (ord(char1) == 32):
        pass
    else:
        string2 = string2 + char1
print(string2)

# 7. Count words in a string.
string1 = str(input("Enter the string:"))
count = 0
temp = len(string1)-1
for i,char1 in enumerate(string1):
    if(char1 == " "):
        count = count + 1
if (string1[temp] != " "):
    count = count + 1
print(count)

# 8. Replace all vowels with ‘*’.
string1 = str(input("Enter the string:"))
vowels = "AEIOUaeiou"
string2 = ""
for i, char1 in enumerate(string1):
    if(char1 in vowels):
        string2 = string2 + "*"
    else:
        string2 = string2 + char1
print(string2)

# 9. Extract digits from a string.
string1 = str(input("Enter the string:"))
vowels = "0123456789"
string2 = ""
for i, char1 in enumerate(string1):
    if(char1 in vowels):
        string2 = string2 + char1
print(string2)

# 10. Find the longest word from a sentence.
str=input("Enter a string:")
word=str.split()
longest=""
for ch in word:
    if(len(ch)>len(longest)):
        longest=ch
print(longest)

# 11. Convert string to title case manually.
string1 = str(input("Enter the string:"))
string2 = ""
if (ord(string1[0])> 96 and ord(string1[0]) < 122):
    temp = ord(string1[0]) - 32
    string2=string2 +chr(temp)
for i, char1 in enumerate(string1):
    if (i != 0 and string1[i-1] == " " and ord(char1) > 96 and ord(char1) < 122):
        temp = ord(char1) - 32
        string2=string2 +chr(temp)
    else:
        string2 = string2 + char1
print(string2)

# 13. Remove special characters from a string.
string1 = str(input("Enter the string:"))
string2 = ""
for i, char1 in enumerate(string1):
    if (ord(char1) > 96 and ord(char1) < 122):
        string2=string2 + char1
print(string2)

# 14. Write a Python program to check substring existence.
string1 = str(input("Enter the string:"))
string2 = str(input("Enter the substring:"))
if string2 in string1:
    print(string2,"=Yes it exists")

# 15. Find the most frequent character in a string.
string1 = str(input("Enter the string:"))
store = ""
count = 0
dict1 = {}
for i, char1 in enumerate(string1):
    if char1 not in store:
        store = store + string1[i]
for i,char1 in enumerate(store):
    count = 0
    for j,char2 in enumerate(string1):
        if(char1==char2):
            count = count + 1
    dict1[store[i]]=count
print(f"Maximun frequency character is={max(dict1, key=dict1.get)} with frequency= {max(dict1.values())}")


# 12. Check if two strings are anagrams.
str_1= str(input("Enter string1:"))
str_1=str_1.lower()
str_2= str(input("Enter string2:"))
str_2=str_2.lower()
freq_1=[]
freq_2=[]
flag = "True"
for i,ch in enumerate(str_1):
    if ch != " ":
        freq_1.append(ch)
for i,ch in enumerate(str_2):
    if ch != " ":
        freq_2.append(ch)
for ch in str_1:
    if ch != " ":
        if ch not in freq_2 :
            flag = "False"
for ch in str_2:
    if ch != " ":
        if ch not in freq_1 :
            flag = "False"
if(flag == "True"):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")