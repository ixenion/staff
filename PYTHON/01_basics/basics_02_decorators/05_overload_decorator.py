from __future__ import annotations
from collections.abc import Sequence


def double_old(input_: int | Sequence[int]) -> int | list[int]:
    if isinstance(input_, Sequence):
        return [i * 2 for i in input_]
    return input_ * 2

x = double_old(12)
# The input was an int, but Mypy has revealed it sees
# the type of x as int | list[int] (in the old long-form spelling).
# Any attempt to use int-only operations with x, such as division, will fail a type check.
# To fix such errors we would be forced to use type narrowing, such as:
# BUT works only when "x" is int
assert isinstance(x, int)
try:
    # works only in mypy
    reveal_type(x)
except:
    print(f'[!] Function "reveal_type" works only in "mypy"')

print(x)


# overload Decorator

from typing import overload


@overload
def double(input_: int) -> int:
    ...


@overload
def double(input_: Sequence[int]) -> list[int]:
    ...


def double(input_: int | Sequence[int]) -> int | list[int]:
    if isinstance(input_, int):
        return input_ * 2
    return [i * 2 for i in input_]

y = double(12)
z = double([12, 13])
try:
    reveal_type(y)
    reveal_type(z)
except:
    print('[!] Function "reveal_type" works only in "mypy"')
    print('y = {}\n{}\nz = {}\n{}'.format(y, type(y), z, type(z)) )
