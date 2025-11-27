import time
def whileloop():
    i = 0 
    while (i<50000):
        # print(i)
        i= i+1
    
def forloop():
    for i in range(0,50000):
        # print(i)
        pass

inital_time = time.time()
forloop()
t1 = time.time() - inital_time
print(f"time for for_loop:{t1}")
time.sleep(5)#sleep for 10 sec 
print("printting while loop after 5 sec delay")
whileloop()
inital_time = time.perf_counter()
t2 = time.time() - inital_time
print(f"time for while_loop:{t2}")

t = time.localtime()
formatted_time = time.strftime("%Y - %m - %d %H:%M:%S", t)
# M- shows minutes, D- shows exact date, 
print(formatted_time)
