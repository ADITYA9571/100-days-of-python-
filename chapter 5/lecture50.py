# "readlines"
# f = open('readlines.txt','r')
# i=0
# while True:
#     i = i+ 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks in student{i} in su is {m1}")
#     print(f"marks in student{i} in su is {m2}")
#     print(f"marks in student{i} in su is {m3}")
#     print(line)

"""writelines"""
f = open('readlines.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close()
