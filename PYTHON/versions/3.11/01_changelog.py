
##################
# SPEED IMPROVED #
##################

'''
1. cpython console launch up to 15%
2. try/except block less time cost
3. Byte code optimization
'''




#################
# NEW TRACEBACK #
#################

# example

# python3.10
# Traceback (most recent call last):
#   File "/home/arix/staff/python/versions/3.11/50_traceback.py", line 12, in <module>
#     print(data["users"]["admins"]["user@mail.ru"]["name"])
# TypeError: 'NoneType' object is not subscriptable

# python3.11
# Traceback (most recent call last):
#   File "/home/arix/staff/python/versions/3.11/50_traceback.py", line 12, in <module>
#     print(data["users"]["admins"]["user@mail.ru"]["name"])
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^
# TypeError: 'NoneType' object is not subscriptable




###################
# EXCEPTION NOTES #
###################

# example

try:
    1 / 0
except Exception as e:
    import datetime
    e.add_note(f"Какой кошмаааар, все упало прямо в: {datetime.datetime.now()}")
    # get list of all notes
    print(e.__notes__)
    raise




###################
# EXCEPTION GROUP #
###################

''' Useful for async tasks. '''

# example

try:
    raise ExceptionGroup("описание группы исключений", [
        ValueError("все плохо"),
        TypeError("какой кошмар"),
        IndexError("что тут вообще происходит?"),
        ValueError("ну офигеть теперь")
        ])
except* ValueError as eg:
    for exc in eg.exceptions:
        print(f"ValueError! Сообщение: {exc}")
except* TypeError as eg:
    for exc in eg.exceptions:
        print(f"TypeError! Сообщение: {exc}")
except* IndexError as eg:
    for exc in eg.exceptions:
        print(f"IndexError! Сообщение: {exc}")

# or if want to process all exception in cycle
except Exception as eg:
    for exc in eg.exceptions:
        print(f"Exception! Сообщение: {exc}")




#################
# TYPE HINT UPD #
#################

'''
1. typeDict
2. Self
3. LiteralString - safe string (not user input)
'''

# example (Slef)

from typing import Self
class Singleton:
    def __new__(cls) -> Self:
        if not hasattr(cls, 'isinstance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)     # True

# example (LiteralString)

from typing import LiteralString

def get_user_by_name(name: LiteralString):
    db.execute(f"select * from {name}")
# safe
get_user_by_name("Alexey")
# not safe
get_user_by_name(input())




############
# TOML LIB #
############




###############
# ASYNCIO UPD #
###############

# example

import asyncio

async def sleep(seconds: int) -> None:
    await asyncio.sleep(seconds)
    print(f"sleeped {seconds}s")

# python3.10
async def old_main():
    tasks = []
    for seconds in (3, 1, 2):
        tasks.append(asyncio.create_task(sleep(seconds)))
    await asyncio.gather(*tasks)

asyncio.run(old_main())

# python3.11
# dont need to create 'tasks' structure
async def main():
    async with asyncio.TaskGroup() as tg:
        for seconds in (3, 1, 2):
            tg.create_task(sleep(seconds))
asyncio.run(old_main())
