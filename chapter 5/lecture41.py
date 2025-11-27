"""Lecture 39 40 bAsed on excercise short hand if-else statement"""
A = int(input("Enter number:"))
B = int(input("Enter number:"))
print("A =", A) if A > B else (print("A == B") if A == B else print("B =", B))
