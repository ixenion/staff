# main idea is that we can pass function to another function as argument
# for specific decorators check
# basics_02_decorators

def f1():
    print("I'm f1")

def f2(f):
    f()

f2(f1)


# wrapper functions

def f3(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    return wrapper

def f4():
    print("Hello")

f3(f4)()
# returns
# Started
# Hello
# Ended

# or another way to write it
f4_2 = f3(f4)
f4_2()


# DECORATORS

@f3         # same as f5 = f3(f5)
def f5():
    print("I'm f5!")

f5()

# but what if "f5" has arguments?
def f6(func):
    def wrapper(*args, **kvargs):
        print("Started f6")
        func(*args, **kvargs)
        print("Ended f6")
    return wrapper

@f6
def f7(param):
    print(param)

f7("Hi from f7!")

# but! what if we want to return something from "f7"?
def f8(func):
    def wrapper(*args, **kvargs):
        print("Started f6")
        val = func(*args, **kvargs)
        print("Ended f6")
        return val
    return wrapper

@f8
def add(x, y):
    return x + y

print(add(2,3))

print("\n")

############
# EXAMPLES #
############

# example 1
import time

def before_after(func):
    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
    return wrapper

class Test:
    @before_after
    def decorated_method(self):
        print("run")

t = Test()
t.decorated_method()


# example 2

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Function took:", time.time() - before, "seconds")
    return wrapper

@timer
def run():
    time.sleep(2)

run()


# example 3 (logging function)
import datetime
import os

def log(func):
    def wrapper(*args, **kvargs):
        with open(os.path.join('etc','logs.txt'), "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")
            val = func(*args, **kvargs)
        return val
    return wrapper

@log
def run2(a, b, c=9):
    print(a+b+c)

run2(1,3, c=9)

