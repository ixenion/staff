import asyncio


message = 0

async def foo():
    global message
    while True:
        await asyncio.sleep(2)
        message += 1
        print(f'[foo] {message}')


async def gee():
    global message
    while True:
        await asyncio.sleep(4)
        message += 1
        print(f'[gee] {message}')


async def main():

    foo_task = asyncio.create_task(foo())
    gee_task = asyncio.create_task(gee())
    await foo_task
    await gee_task

async def main2():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(foo())
        tg.create_task(gee())


asyncio.run(main2())
