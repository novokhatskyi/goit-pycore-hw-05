from typing import Callable

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))