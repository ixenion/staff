import asyncio

async def waiter(event):
    print('waiting for it ...')
    await event.wait()
    print('... got it!')

async def payload(event: asyncio.Event):
    for sec in range(1, 101):
        await asyncio.sleep(1)
        print(f'seconds: {sec}')
        if sec == 4:
            event.set()
            break

async def main():
    # Create an Event object.
    event = asyncio.Event()

    # Spawn a Task to wait until 'event' is set.
    waiter_task = asyncio.create_task(waiter(event))
    payload_task = asyncio.create_task(payload(event))

    # Sleep for 1 second and set the event.
    # await asyncio.sleep(3)
    # event.set()

    # Wait until the waiter task is finished.
    await payload_task
    await waiter_task

asyncio.run(main())
