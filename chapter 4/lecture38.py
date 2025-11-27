"""raising custom errors in pythin"""
a = int (input("Enter a number betwenn 5-10"))
if (a<5 or a>10):
    raise ValueError("Value error should be between 5-10")
