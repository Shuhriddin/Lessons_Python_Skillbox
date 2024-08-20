# TODO здесь писать код

from typing import Callable

def how_are_you(func: Callable) -> Callable:
    """Декоратор для выполнение функция"""
    def wrapper(*args, **kwargs):
        answer = input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func(*args, **kwargs)
        return answer
    return wrapper

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()
print(how_are_you.__doc__)
