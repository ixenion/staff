import asyncio


async def calcs():
    loop = asyncio.get_event_loop()
    task2 = loop.create_task(circle())
    for i in range(2):
        print(f'f1 {i}')
        await asyncio.sleep(1)
    task2.cancel()

async def circle():
    for i in range(4):
        print(f'f2 {i}')
        await asyncio.sleep(1)

async def f3():
    for i in range(6):
        print(f'f3 {i}')
        await asyncio.sleep(1)

async def main():
    loop = asyncio.get_event_loop()
    task1 = loop.create_task(calcs())
    task3 = loop.create_task(f3())
    await task3

asyncio.run(main())
