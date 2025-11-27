# EXCERSICE 7!!!
import os
files = os.listdir("Photos")
# os.rename("Cluttered/filename.txt", "cluttered/renamed.txt")
i = 1
for file in files:
    print(file)
    if(file.endswith(".png")):
        os.rename(f"Photos/{file}", f"Photos/{i}.png")
        i=i+1

print("done")