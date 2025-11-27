import threading 
# concurrent.future
import time
from concurrent.futures import ThreadPoolExecutor 
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

# time1= time.perf_counter()
# func(4)
# func(2)
# func(1)
# time2= time.perf_counter()
# print(time1-time2)

# time1= time.perf_counter()
# t1 = threading.Thread(target =func, args= [4])
# t2 = threading.Thread(target =func, args= [2])
# t3 = threading.Thread(target =func, args= [1])

# t1.start()
# t2.start()
# t3.start()
# time2= time.perf_counter()
# print(time1-time2)

# print(dir(threading.Thread))

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future = executor.submit(func,3)
        # print(future.result())
        # future = executor.submit(func,2)
        # print(future.result())
        # future = executor.submit(func,5)
        # print(future.result())
        future1 = executor.submit(func,3)
        future2 = executor.submit(func,2)
        future3 = executor.submit(func,5)
        print(future1.result())
        print(future2.result())
        print(future3.result())
# map funnction

poolingDemo()