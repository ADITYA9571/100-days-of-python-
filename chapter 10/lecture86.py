# # walrus operator (:=) // assign a value to a variable within an expression
# b = True
# print(b:=False)
# if (n := len("walrus")) > 3:
#     print(f"Length is {n}")
# numbers = [1,2,3,4,5]
# while (n:= len(numbers))> 0 :
#     print(numbers.pop())
# numbers.append(10)
# print(numbers)
"""type 1"""
food1 = []    #food2 = list()
while True:
    food = input("What food you want?:")
    if food == "quit":
        break
    food1.append(food)
print(food1)
"""using walrus"""
games = []
while(game := input("you like to play with:"))!="exit":
    games.append(game)
print(games)