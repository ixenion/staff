import asyncio

async def foo():
    i = 0
    while True:
        i += 1
        await asyncio.sleep(1)
        print(f'[foo] {i}')
        
        if i == 3:
            # get the event loop
            loop = asyncio.get_running_loop()
            # schedule a stop to the event loop
            # returns Exception. Breaks all the code.
            # loop.close()
            # schedule a stop to the event loop
            # returns Exception. Breaks all the code.
            loop.stop()

    print(f'[foo] Done!')
    pass


async def bar():
    for i in range(5):
        await asyncio.sleep(0.5)
        print(f'[bar] {i}')
    print(f'[bar] Done!')
    pass


async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())
    await task2
    await task1

asyncio.run(main())
