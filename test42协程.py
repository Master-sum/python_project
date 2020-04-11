import asyncio
import datetime

async def dis():
    loop = asyncio.get_running_loop()
    end = loop.time()+6
    print(loop.time())
    while True:
        print(datetime.datetime.now())
       # print(loop.time())
        if (loop.time() +1)>=end:
            break
        await asyncio.sleep(1)

asyncio.run(dis())