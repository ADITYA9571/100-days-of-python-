# sleep mthod is a time waste
# try for asynchronous io
# await- waits for fuction completion
# how to download a file from a url
import time 
import asyncio
import requests
async def function1():
    # await asyncio.sleep(1)
    # print("Func 1") 
    url = "https://img.freepik.com/premium-photo/motion-blurred-racetrack-vertical-poster-format_146508-3888.jpg"
    response = requests.get(url)
    open("amazon1.jpg","wb").write(response.content)

# async def function2():
#     # await asyncio.sleep(2)
#     # print("Func 2")
#     url = "https://m.media-amazon.com/images/I/61mOVGinDdL._SL1500_.jpg"
#     response = requests.get(url)
#     open("amazon2.ico","wb").write(response.content) 
# async def function3():
#     # await asyncio.sleep(3)
#     # print("Func 3")
#     url = "https://m.media-amazon.com/images/I/61mOVGinDdL._SL1500_.jpg"
#     response = requests.get(url)
#     open("amazon3.ico","wb").write(response.content)     

async def main():
    # task = asyncio.create_task(function1())
    # await function2()
    # await function3()
    # L = await asyncio.gather(
        await function1()
        # await function2()
        # await function3()    
    # )
asyncio.run(main())
