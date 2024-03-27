import asyncio
from asyncio import Event
from typing import Type

class Police(object):

    def __init__(self, phone:str):

        self.__mobile = phone
        self.position = 0

    def call_police(self):
        print(f'Police have been informed')

    async def observe(self, circle:int) -> None:
        while True:
            for step in range(circle):
                await asyncio.sleep(1)
                self.position = step
                print(f'[Police] position {step}/{circle}')
    
    async def hurry_to_accident(self, speed:int) -> None:
        for i in range(10):
            await asyncio.sleep(1/speed)
        print(f'[Police] came to the place of the accident.')


class Owner(object):
    
    def __init__(self, phone:str):
        self.__mobile = phone

    def call_owner(self):
        print(f'Owner has been informed')




class Alarm(object):

    def __init__(self):
        self.event = Event()
        pass

    async def init(self):
        loop = asyncio.get_event_loop()
        # loop.create_task(self.stop_alarm())
        loop.create_task(self.start_alarm())
        # self.task2 = asyncio.create_task(self.start_alarm())
        # await self.task2

    async def stop_alarm(self):
        while True:
            await asyncio.sleep(1)
            print(f'[Alarm] sirens are Silent.')

    async def start_alarm(self):
        while True:
            # await self.event.wait()
            await asyncio.sleep(1)
            print(f'[Alarm] sirens are Wailing.')


# Lock class
class Lock(object):

    def __init__(self):
        self.subscribers = []
        self.on_lock_broken = Event()

    def lock_broken(self):
        self.on_lock_broken.set()

    def add_subscriber_for_lock_broken_event(self, subscriber: Type):
        self.subscribers.append(subscriber)

    def remove_subscriber_for_lock_broken_event(self, subscriber):
        pass
    
    def __call__(self):
        print(f'call')
        pass

async def main():

    loop = asyncio.new_event_loop()

    alarm = Alarm()
    await alarm.init()
    lock = Lock()
    lock.add_subscriber_for_lock_broken_event(alarm)


asyncio.run(main())


