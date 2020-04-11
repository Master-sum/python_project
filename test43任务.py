import asyncio
async def test1():
    print('211')
async def test2():
    print('6877')
async def main():
    task1 = asyncio.create_task(test1())
    task2 = asyncio.create_task(test2())
    await task1,task2

asyncio.run(main())