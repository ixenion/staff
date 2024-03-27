from multiprocessing import Process, Queue
from time import sleep
from typing import Callable


res = {}

def process(func:Callable):
    def wrapper(*args, **kwargs):
        process = Process(target=func, args=args, kwargs=kwargs)
        process.start()
        # process.join()
        # print(process.)
    return wrapper

@process
def foo(msg:str, delay:int) -> bool:
    sleep(delay)
    print(msg)
    return True




res1 = foo('123', delay=3)
res2 = foo('321', delay=1)


print(res1)
print(res2)


foo('asd', delay=2)
