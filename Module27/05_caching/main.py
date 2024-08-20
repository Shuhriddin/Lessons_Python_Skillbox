# TODO здесь писать код
from typing import Callable
def memoize(func: Callable) -> Callable:
    """ Декоратор для кэширования результатов функции.
    Args:
        func (callable): Функция, результаты которой нужно кэшировать.
    Returns:
        callable: Обертка, которая кэширует результаты функции.
    """
    cache = {}
    def wrapper(number: int) -> int:
        """ Обертка для функции с кэшированием результатов.
        Args:
            number (int): Число, для которого нужно вычислить результат.
        Returns:
            int: Результат вычисления функции для данного числа.
        """
        if number not in cache:
            cache[number] = func(number)
        return cache[number]
    return wrapper
@memoize
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
