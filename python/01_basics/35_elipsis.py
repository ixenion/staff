from typing import List
from typing import Tuple
# since py3.9 deprecated
#from typing import Callable
# instad use
from collections.abc import Callable
from typing import Any

# use elipsis as placeholder
def do_nothing():
    ...




def f() -> Tuple[int, str, float]:
    return 1, 'foo', 1.5

# Here elipsys says that this is a temple
# of integers that is variable in length.
def g() -> Tuple[int, ...]:
    x: List[int] = [1, 2, 3, 4]
    return tuple(x)



def get_function_info(func: Callable[..., Any]) -> str:
    return f'{func.__name__}(...)'
