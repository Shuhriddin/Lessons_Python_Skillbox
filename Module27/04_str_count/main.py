# TODO здесь писать код

from typing import Callable
def counter(func: Callable) -> Callable:
    """Декоратор подсчитывает, сколько раз вызывается функция"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция была вызвана {wrapper.count} раз")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@counter
def add(num1, num2):
    result = num1 + num2
    print("Ответ:", result)
    return result

if __name__ == '__main__':
    add(5, 5)
    add(3, 7)
    add(6, 4)