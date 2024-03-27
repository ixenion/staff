# link:
# https://www.pythontutorial.net/python-basics/python-lambda-expressions/

"""
Python lambda expressions allow you to define anonymous functions.

Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

A lambda expression typically contains one or more arguments, but it can have only one expression.

The following shows the lambda expression syntax


lambda parameters: expression

def anonymous(parameters):
    return expression

"""

# Without lambda expression:
def get_full_name1(first_name, last_name, formatter):
    return formatter(first_name, last_name)

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"

def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"

full_name = get_full_name1('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name1('John', 'Doe', last_first)
print(full_name) #  Doe, John
# output:
# John Doe
# Doe, John


# With lambda expression:
def get_full_name2(first_name, last_name, formatter):
    return formatter(first_name, last_name)

full_name = get_full_name2(
    'John',
    'Doe',
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(full_name)

full_name = get_full_name2(
    'John',
    'Doe',
    lambda first_name, last_name: f"{last_name} {first_name}"
)
print(full_name)
# output:
# John Doe
# Doe, John


# Timeit
from timeit import Timer

def test1():
    full_name = get_full_name1('John', 'Doe', last_first)
    return
def test2():
    full_name = get_full_name2(
        'John',
        'Doe',
        lambda first_name, last_name: f"{last_name} {first_name}"
    )
    return



measure1 = sum(Timer(test1).repeat(repeat=1, number=100_000))
measure2 = sum(Timer(test2).repeat(repeat=1, number=100_000))
print(measure1)
print(measure2)
print(f"{round((measure2/measure1 - 1)*100)}%")
