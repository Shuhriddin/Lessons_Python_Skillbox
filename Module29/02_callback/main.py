# TODO здесь писать код

from typing import Callable, Optional
import functools

app = dict()

def callback(_name_function: Optional[Callable] = None, *, route: str = None) -> Callable:
    def decorator_callback(name_function: Callable) -> Callable:
        """ Декоратор функции обратного вызова """
        app[route] = name_function
        @functools.wraps(name_function)
        def wrapper(*args, **kwargs):
            function_call = name_function(*args, **kwargs)
            return function_call
        return wrapper
    if _name_function is not None:
        return decorator_callback
    return decorator_callback(_name_function)

@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# print(app)