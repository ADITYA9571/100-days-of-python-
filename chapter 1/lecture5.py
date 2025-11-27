"""
This script demonstrates different ways to comment out code in Python.
"""

# Use `#` for single-line comments.
# This is the most common and recommended method.

# Alternatively, use triple quotes (""" or ''') to comment out blocks temporarily.
# But remember: triple quotes are actually string literals, not true comments.

# Tip: In editors like VS Code, you can use Ctrl + / to toggle comments on selected lines.

print("We learned commenting out")
#try to use escape sequence syntax 
print("Lets deep dive into the escape sequeces")
print("This is a backslash: \\")
print('It\'s fine.')
print("He said: \"Hello!\"")
print("Line1\nLine2")
print("Hello\tWorld")
print("123\rXY")
print("Hello\bWorld")
print("Hello\fWorld")
print("\a")	
print("Hello\vWorld")
print("\101")	
print("\x41")
print("\N{COPYRIGHT SIGN}")
print("\u00A9")
print("\U0001F600")
print("Carriage\rReturn")
print("Backspace\b111")
print("Form\ffeed")
print("\afor alert")
print("Vertical\vMove: This move varies on the system to system")
print("\102 \\102 prints as Octal 102 = Decimal 66 = Unicode 'B'")
print("\x42 \\x42 prints Hex 42 = Decimal 66 = 'B'")
print("We can even print directly using unicode syntax as \\u00A9 like this \u00A9")
print("Harry", 6, 5, 2025, sep="/", end="come")
print("wOOW",6,"may","shit",sep="~",end="go\n")
print("The end",end="")