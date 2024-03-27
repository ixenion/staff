from time import time, sleep
from collections import defaultdict

# first we define a dictionary to save the function timings.
# we use 'defaultdict' so an empty array value will automatically be created whenever a
# non-existing key is added.
timings = defaultdict(lambda: [])

# next we define the 'timer' decorator which computes the function execution time.
def timer(function):
    def wrapper(*args, **kvargs):

        start_time = time()
        result = function(*args, **kvargs)
        end_time = time()
        total_time = end_time - start_time

        timings[function.__name__].append(total_time)
        return result
    return wrapper

# now we can use this decorator to log the timings of all functions we decorate
@timer
def run_me_once():
    sleep(1)
    return "woohoo"

run_me_once()

@timer
def run_me_twice():
    sleep(2)

run_me_twice()
run_me_twice()

print(timings)
