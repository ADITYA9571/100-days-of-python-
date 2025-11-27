"""python decorators """
def toll(fx):
    def wrapper(*args, **kwargs):
        amt = args[0]  # Assuming amt is the first positional argument
        print("Welcome to Raje Toll Plaza")
        print(f"Checking balance before deducting {amt}")
        fx(*args, **kwargs)
        print(f"{amt} has been processed.")
        print("Thanks for visiting us")
    return wrapper

@toll

def pay(amt):
    print(f"{amt} is deducted!") 

# pay = toll(pay)

pay(110)
