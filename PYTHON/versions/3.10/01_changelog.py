
#######################
# BETTER TYPE HINTING #
#######################

# python 3.10

class User:
    pass

def get_user_by_id(user_id: str | int) -> User | None:
    return User()

# before python 3.10
from typing import Union, Optional

def get_user_by_id2(user_id: Union[str, int]) -> Optional[User]:
    return User()


####################
# BETTER TRACEBACK #
####################

print("Hello wrold")

# OUTPUT
# File "/home/arix/staff/python/versions/3.10/test.py", line 1
#     print("Hello world"
#          ^
# SyntaxError: '(' was never closed

# now it tels what and where happened
# )

####################
# PATTERN MATCHING #
####################

# example 1
# basic use of 'match'

# new (cheks that it list and contains two values)
def run_action(user_input: list) -> None:
    match user_input:
        # check if value is more than 50px
        case 'left', value if int(value) > 50:
            print("something...")
        case action, value:
            print(f"{action=}, {value=}")
        # check command
        case 'left'|'right'|'top'|'bottom' as action, value:
            print(f"Go to {action=}, by {value=}px")
        case 'shoot', *coords:
            print(f"Shoot by coords: {coords}")
        # here comma is no unpack user_input list
        case 'quit', :
            print(f"Dosvidylli!")
        case _:
            print(f"Wrong command")

run_action('go_left 100'.split())
run_action('left 100'.split())
run_action('shoot 100 200 500 1000'.split())
run_action('quit'.split())

# old
def run_action2(user_input: list) -> None:
    if isinstance(user_input, list) and len(user_input) == 2:
        action, value = user_input
        print(f"{action=}, {value=}")
    else:
        print(f"Wrong command")

run_action2('go_left 100'.split())


# example 2
# dictionary parsing

user_action = {
        "id": 123,
        "action": "left",
        "value": 50,
        "timestamp": 1640434565,
        "user_group": 11,
        "cash": 2_000_000
        }

match user_action:
    # str(action) checks that field is string type
    case {"action": str(action), "value": int(value)}:
        print(f"{action=}, {value}")

# OUTPUT
# action='left', 50


# example 3
# usage of class and dictionary in match|case

class UserInput:
    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value

def run_horizontaly(user_input: UserInput | dict):
    match user_input:
        # class
        # if want pattern wwithout keywalues see example 4
        case UserInput(action='left'|'right', value=value):
            print(f"Moving horizontaly on {value} px")
        # dictionary
        case {"action": "left"|"right", "value": value}:
            print(f"Moving horizontaly on {value} px")
        case _:
            pass

input1 = UserInput("left", 150)
input2 = {"action": "right", "value": 300}
input3 = UserInput("top", 20)

run_horizontaly(input1)     # Moving horizontaly on 150 px
run_horizontaly(input2)     # Moving horizontaly on 300 px
run_horizontaly(input3)     # 


# example 4
# class properties without keywords

class UserInput2:

    __match_args__ = ("action", "value")

    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value

def run_horizontaly2(user_input: UserInput | dict):
    match user_input:
        # class
        case UserInput('left'|'right', value):
            print(f"Moving horizontaly on {value} px")
        # dictionary
        case {"action": "left"|"right", "value": value}:
            print(f"Moving horizontaly on {value} px")
        case _:
            pass


# example 5
# ??

class Ok:
    __match_args__ = ("value", )
    def __init__(self, value):
        self.value = value

class Err:
    __match_args__ = ("value", )
    def __init__(self, value):
        self.value = value

Result = Ok | Err

def parse(value: str) -> Result:
    if value.isnumeric():
        return Ok(int(value))
    return Err(f"{value} is not numeric!")

match parse("123"):
    case Ok(value):
        print(f"result is ok, value is {value}")
    case Err(message):
        print(f"result is error, message is {message}")
