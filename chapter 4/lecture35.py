"""Learning about else with for and while loop"""
for i in range(1,11,2):
    print(i)

print("3 parameter for loop")
for i in range(5,8):
    print(i)
#else:
print("Else wil not work on brake")

for i in range(9,15):
    print(i)
    if i==10 :
        break
else:
    print("Else wil not work on brake")

while i<=15:
    print(i)
    i =1+i
