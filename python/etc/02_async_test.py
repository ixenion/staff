import asyncio

async def count():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)

async def handle():
    print('Before response')
    await asyncio.sleep(2)
    print('After response')


async def main():
    task1 = asyncio.create_task(count())
    task2 = asyncio.create_task(handle())
    await task1

server = SomeClass()

asyncio.run(main())

server.clients

print('after main')


