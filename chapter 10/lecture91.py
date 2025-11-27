# generators 
# A generator is a special kind of function that can yield values one at a time instead of returning them all at once.
"""
memory efficient, lazy evaluation, performance improvement
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)
