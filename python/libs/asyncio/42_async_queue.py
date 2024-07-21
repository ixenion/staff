import asyncio


async def foo(queue):
    count = 0
    while True:
        print(f"from foo: {count}")
        # Get remainder from division
        if count % 2 == 0:
            await queue.put(count)
        count += 1
        await asyncio.sleep(1)

async def handler(queue):
    while True:
        item = await queue.get()
        yield item


async def main():
    
    queue = asyncio.Queue(maxsize=0)
    task1 = asyncio.create_task(foo(queue))

    async for item in handler(queue):
        print(item)

    # await task1

asyncio.run(main())
