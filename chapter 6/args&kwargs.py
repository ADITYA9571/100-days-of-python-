def mixed_example(arg1, *args, **kwargs):
    print("arg1:", arg1)
    print("args:", args)
    print("kwargs:", kwargs)

mixed_example(10, 20, 30, name="Bob", job="Engineer")

def add_numbers(*args):
    print(args)
    return sum(args)

add_numbers(1, 2, 3, 4)

def print_info(**kwargs):
    print(kwargs)

print_info(name="Alice", age=30)
print_info(name="Aditya", age=35)
