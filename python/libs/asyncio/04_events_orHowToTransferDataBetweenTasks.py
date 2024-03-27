# main purpose of that example is to
# show how to transfer data between tasks
# with asyncio.Event()
# tutorial: https://youtu.be/PZCymurJEa0


from random import randint
import asyncio

new_data = None
event = asyncio.Event()


async def task_a():
    global new_data

    while True:
        new_data = randint(0, 100)
        event.set()     # event happened
        await asyncio.sleep(2)

async def task_b():
    while True:
        await event.wait()
        print(f"new data: ", new_data)
        event.clear()   # stop endless printing of the same number

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    event_loop.create_task(task_a())
    event_loop.create_task(task_b())
    event_loop.run_forever()
    print('123')
