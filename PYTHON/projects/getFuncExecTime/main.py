from core import get_function_execution_time, rename, return_execution_time

# TEST FUNCTIONS

# @rename('BRACKETS')
# @return_execution_time
# def brackets_check():
#     for _ in range(10_000):
#         var_list = []
#         del var_list

# @rename('FUNCTION')
# @return_execution_time
# def function_check():
#     for _ in range(10_000):
#         var_list = list()
#         del var_list

@rename('ISINSTANCE')
@return_execution_time
def func1():
    for _ in range(10_000):
        # var = 1
        isinstance(1, int)

@rename('TYPE')
@return_execution_time
def func2():
    for _ in range(10_000):
        # var = 1
        type(1) == int


if __name__ == "__main__":
    # get_function_execution_time(brackets_check, function_check)
    get_function_execution_time(func1, func2)
