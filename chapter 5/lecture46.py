"""learning about os module """
import os
# if not os.path.exists("day_46"):
#     os.mkdir("day_46")
# os.rename("day_46","day_4646")
# for i in range(0,5):
#     os.makedirs(f"day_46/file/what{i+1}")
# print(os.getcwd())
# os.chdir("C:/aditya123/self_coding/pythonlanguageCWH/code/chapter 5")
# print(os.getcwd())
os.chdir("C:/aditya123/self_coding/pythonlanguageCWH/code/chapter 5/day_46/file")
folders = os.listdir("C:/aditya123/self_coding/pythonlanguageCWH/code/chapter 5/day_46/file")
print(folders)
for folder in folders:
    print(folders)

