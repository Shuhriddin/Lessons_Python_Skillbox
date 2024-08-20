# TODO здесь писать код
import functools
def singleton(cls):
    """Декоратор класса. Превращает класс в синглтон (может иметь только один инстанс)"""
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
    wrapper_singleton.instance = None  # cache
    return wrapper_singleton


@singleton
class Example:
    pass

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)