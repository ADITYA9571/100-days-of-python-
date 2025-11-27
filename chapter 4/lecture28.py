print("string formatting in python")
letter = "I am {0} and i am from {1}"
name = "Aditya"
country = "Adityanand"
print(letter.format(name,country))
print(f"I am {name} and i am from {country}")
print(f"we can use f-strings as: I am {{name}} and i am from {{country}}")
price = 49.002242
txt = f"for only {price:.2f} dollars!!"
print(txt)
print(txt.format())
print(type(f"{2*20}"))