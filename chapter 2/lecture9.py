"""
In this lecture we are going to learn about typecasting 
The need occured when the stuffs like concating occurs 
int(), float(), str(), ord(), hex(), oct(), tuple(), set(), 
"""
# 🔹 Integer to Float
int_value = 10
float_value = float(int_value)
print("Integer to Float:", float_value)  # Output: 10.0

# 🔹 Float to Integer
float_value = 3.99
int_value = int(float_value)
print("Float to Integer:", int_value)    # Output: 3

# 🔹 Integer to String
int_value = 100
str_value = str(int_value)
print("Integer to String:", str_value)   # Output: "100"

# 🔹 String to Integer (only numeric strings)
str_value = "50"
int_value = int(str_value)
print("String to Integer:", int_value)   # Output: 50

# 🔹 String to Float (only numeric strings)
str_value = "3.14"
float_value = float(str_value)
print("String to Float:", float_value)   # Output: 3.14

# 🔹 Float to String
float_value = 2.718
str_value = str(float_value)
print("Float to String:", str_value)     # Output: "2.718"

# 🔹 Integer to Complex
int_value = 7
complex_value = complex(int_value)
print("Integer to Complex:", complex_value)  # Output: (7+0j)

# 🔹 String to Complex
str_value = "4+3j"
complex_value = complex(str_value)
print("String to Complex:", complex_value)   # Output: (4+3j)

# 🔹 List to Tuple
list_value = [1, 2, 3]
tuple_value = tuple(list_value)
print("List to Tuple:", tuple_value)     # Output: (1, 2, 3)

# 🔹 Tuple to List
tuple_value = (4, 5, 6)
list_value = list(tuple_value)
print("Tuple to List:", list_value)      # Output: [4, 5, 6]

# 🔹 List to Set (removes duplicates)
list_value = [1, 2, 2, 3, 4]
set_value = set(list_value)
print("List to Set:", set_value)         # Output: {1, 2, 3, 4}

# 🔹 Set to List
set_value = {5, 6, 7}
list_value = list(set_value)
print("Set to List:", list_value)        # Output: [5, 6, 7]

# 🔹 String to List (character split)
str_value = "hello"
list_value = list(str_value)
print("String to List:", list_value)     # Output: ['h', 'e', 'l', 'l', 'o']

# 🔹 List to String (using join)
list_value = ['h', 'e', 'l', 'l', 'o']
str_value = "".join(list_value)
print("List to String:", str_value)      # Output: "hello"

# 🔹 Boolean to Integer
bool_value = True
int_value = int(bool_value)
print("Boolean to Integer:", int_value)  # Output: 1

# 🔹 Integer to Boolean
int_value = 0
bool_value = bool(int_value)
print("Integer to Boolean:", bool_value) # Output: False
