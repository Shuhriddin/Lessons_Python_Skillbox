# TODO здесь писать код

from datetime import datetime
from typing import Callable, Any

def logging(func: Callable) -> Callable:
    """Декоратор для логгирования функций"""
    def wrapper(*args, **kwargs) -> Any:
        print(func.__name__)
        print(func.__doc__)
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            with open('function_errors.log', 'a', encoding="UTF-8") as error_file:
                error_file.write(f'Функция: {func.__name__}\n')
                error_file.write(f'Ошибки: {str(e)}\n')
                error_file.write(f'Время фикцации: {datetime.now()}\n\n')
    return wrapper

@logging
def square_numbers():
    """Функция вернуть список квадратов нечетных чисел от 0 до 99."""
    result = [i**2 for i in range(100) if i % 2 != 0]
    return result

@logging
def divider(num1, num2):
    """Разделить два числа"""
    return num1 / num2

print(square_numbers())
print(divider(10, 0))

