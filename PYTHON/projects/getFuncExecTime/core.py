import pandas as pd
from pathlib import Path
from statistics import mean, median, stdev
from tabulate import tabulate
from time import time
from typing import Callable, Dict


# FUNCTIONS TO PRINT AND SAVE TABLE

ALLOWED_PATH_CHARS = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_.-/\\йцукенгшщзхъфывапролджэячсмитьбюёЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'

def assert_path_allowed(path: Path) -> Path:
	origin = allowed = str(path)
	allowed = allowed.replace(':', '_').replace(' ', '_')
	allowed = ''.join([x for x in allowed if x in ALLOWED_PATH_CHARS])
	new = Path(allowed)
	if origin != allowed:
		print(f'Specified report path {path} is not allowed. Using {new} instead.')
	return new

class Table:

    def __init__(self, indicators: Dict[str, str | float | int]):
        self._df = pd.Series(indicators)

    def __str__(self) -> str:
        # return self._df.to_markdown(headers=[], tablefmt="grid")
        items = []
        for indicator, value in self._df.to_dict().items():
            is_ok = True
            # if isinstance(value, Threshold):
            # 	is_ok = value.validate(indicator, quite=True)
            # 	indicator += f' [{value.str_rounded(True)}]'
            # 	value = value.str_rounded()
            if isinstance(value, float):
                # rounding
                # value = f'{value:0>5.2f}'
                pass
            else:
                value = str(value)
            # if not is_ok:
            #     value = style(value, fg=typer.colors.YELLOW)
            items.append([indicator, value])
        return tabulate(items, headers=[], tablefmt='fancy_grid')

    def save(self, path: Path | str):
        items = {}
        for indicator, value in self._df.to_dict().items():
            # if isinstance(value, Threshold):
            #     value.validate(indicator)
            #     value = float(value)
            items[indicator] = value
        path = assert_path_allowed(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.Series(items).to_excel(path, header=False)


# FUNCTIONS TO GET EXECUTION TIME

def return_execution_time(func: Callable):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        delta = t2 - t1
        yield delta
    return wrapper

def rename(newname):
    def wrapper(f):
        f.__name__ = newname
        return f
    return wrapper

def _cycle_function_under_test(cycles: int, func: Callable) -> float:
    val = []
    for _ in range(cycles):
        val.extend(func() )
    return mean(val), median(val), stdev(val)

def get_function_execution_time(*args: Callable, cycles: int = 2000):
    for func in args:
        _mean, _median, _stdev = _cycle_function_under_test(cycles, func)
        result = Table({
                f'{func.__name__}': '',
                'Mean': _mean,
                'Median': _median,
                'Stdev [%]': ( _stdev / _median ) * 100
                })
        print(result)
