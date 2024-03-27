# tutorial
# https://realpython.com/python-with-statement/#creating-custom-context-managers


# In general, context managers and the with statement aren’t limited to
# resource management. They allow you to provide and reuse common setup and
# teardown code. In other words, with context managers, you can perform any
# pair of operations that needs to be done before and after another operation
# or procedure, such as:

# Open and close
# Lock and release
# Change and reset
# Create and delete
# Enter and exit
# Start and stop
# Setup and teardown

# You can provide code to safely manage any of these pairs of operations in
# a context manager. Then you can reuse that context manager in with statements
# throughout your code. This prevents errors and reduces repetitive boilerplate code.
# It also makes your APIs safer, cleaner, and more user-friendly.


# Writing a Sample Class-Based Context Manager
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        print(exc_type, exc_value, exc_tb, sep="\n")
# If an exception occurs, then exc_type, exc_value, and exc_tb hold
# the exception type, value, and traceback information, respectively.

with HelloContextManager() as hello:
    print(hello)
    print(hello)
    # hello[100]
# error
# with HelloContextManager as hello:
#     print(hello)
print('\n#################\n')

# Handling Exceptions in a Context Manager
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True

with HelloContextManager() as hello:
    print(hello)
    hello[100]

print("Continue normally from here...")


# WritableFile implements the context management protocol and supports
# the with statement, just like the original open() does,
# but it always opens the file for writing using the "w" mode.
# Here’s how you can use your new context manager:

class WritableFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

with WritableFile("hello.txt") as file:
    file.write("Hello, World!")



# Redirecting the Standard Outpu
# For example, say you need to temporarily redirect the standard output,
# sys.stdout, to a given file on your disk.
# To do this, you can create a context manager like this:
import sys

class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.saved_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.saved_output

# This context manager takes a file object through its constructor.
# In .__enter__(), you reassign the standard output, sys.stdout, to an instance
# attribute to avoid losing the reference to it. Then you reassign the standard
# output to point to the file on your disk.
# In .__exit__(), you just restore the standard output to its original value.

# To use RedirectedStdout, you can do something like this:

with open("hello.txt", "w") as file:
    with RedirectedStdout(file):
        print("Hello, World!")
    print("Back to the standard output...")
# The outer with statement in this example provides the file object that you’re
# going to use as your new output, hello.txt. The inner with temporarily
# redirects the standard output to hello.txt, so the first call to print()
# writes directly to that file instead of printing "Hello, World!" on your screen.
# Note that when you leave the inner with code block, the standard output goes back to its original value.

# RedirectedStdout is a quick example of a context manager that doesn’t have a
# useful value to return from .__enter__(). However, if you’re only redirecting
# the print() output, you can get the same functionality without the need
# for coding a context manager. You just need to provide a file argument to print() like this:
with open("hello.txt", "w") as file:
    print("Hello, World!", file=file)



# Measuring Execution Time

from time import perf_counter
from time import sleep

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = perf_counter()

with Timer() as timer:
    # Time-consuming code goes here...
    sleep(0.5)
print(f"\nTimer result: {timer()}")
# With Timer, you can measure the execution time of any piece of code.
# In this example, timer holds an instance of the lambda function that
# computes the time delta, so you need to call timer() to get the final result.


# Creating Function-Based Context Managers

from contextlib import contextmanager

@contextmanager
def hello_context_manager():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")
with hello_context_manager() as hello:
    print(hello)
# OUTPUT
# Entering the context...
# Hello, World!
# Leaving the context...

# In this example, you can identify two visible sections in hello_context_manager().
# Before the yield statement, you have the setup section. There, you can
# place the code that acquires the managed resources. Everything before the
# yield runs when the flow of execution enters the context.

# After the yield statement, you have the teardown section, in which you can
# release the resources and do the cleanup. The code after yield runs
# at the end of the with block. The yield statement itself provides the object
# that will be assigned to the with target variable.



# Opening Files for Writing: Second Version
#from contextlib import contextmanager

@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    try:
        yield file
    finally:
        file.close()

with writable_file("hello.txt") as file:
    file.write("Hello, World!")


# Mocking the Time
from time import time
@contextmanager
def mock_time():
    global time
    saved_time = time
    time = lambda: 42
    yield
    time = saved_time
with mock_time():
    print(f"Mocked time: {time()}")
# OUTPUT
# Mocked time: 42
# Back to normal time
#time()
# OUTPUT
# 1616075222.4410584


# Writing Good APIs With Context Managers
class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.level -= 1

    def print(self, text):
        print("    " * self.level + text)

with Indenter() as indent:
    indent.print("hi!")
    with indent:
        indent.print("hello")
        with indent:
            indent.print("bonjour")
    indent.print("hey")
# OUTPUT
# hi!
#     hello
#         bonjour
# hey


# Creating an Asynchronous Context Manager

# site_checker_v1.py

import aiohttp
import asyncio

class AsyncSession:
    def __init__(self, url):
        self._url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self._url)
        return response

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        await self.session.close()

async def check(url):
    async with AsyncSession(url) as response:
        print(f"{url}: status -> {response.status}")
        html = await response.text()
        print(f"{url}: type -> {html[:17].strip()}")

async def main():
    await asyncio.gather(
        check("https://realpython.com"),
        check("https://pycoders.com"),
    )

asyncio.run(main())
