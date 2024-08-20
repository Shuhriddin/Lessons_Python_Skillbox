# TODO здесь писать код

import time
from typing import Callable, Any
import functools

def loading(seconds: int) -> Callable:
    """Декоратор функция для замедления выполнения"""
    def func_slowly(func: Callable) -> Callable:
        @functools.wraps(func_slowly)
        def wrapper(*args, **kwargs) -> Any:
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return func_slowly

@loading(2)
def some_function():
    print("Функция выполняется через 2 секунд(ы)")

some_function()
print(loading.__doc__)
