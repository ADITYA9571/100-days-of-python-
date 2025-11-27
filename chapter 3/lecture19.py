print("Emulated do-while loop")
count = 0
while True:
    print(count)
    count += 1
    if count == 5:
        print("loop broken")
        break
print("break statement will exit the loop")
for i in range(1,15):
    print("5 X",i,(5*i))
    if i == 10:
        break

print("continue statement will skip that particular iteration")
for i in range(1,15):
    if i%2 == 0:
        continue
    print("5 X",i,(5*i))
