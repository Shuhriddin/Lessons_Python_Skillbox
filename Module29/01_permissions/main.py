# TODO здесь писать код

from typing import Callable


def check_permissions(name: str):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if name in user_permissions:
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}")
        return wrapper
    return decorator


user_permissions = ['admin']
@check_permissions('admin')
def delete_site():
    print("Удаляем сайт")
@check_permissions('user_1')
def add_comment():
    print("Добавляем комментарий")

delete_site()
try:
    add_comment()
except PermissionError as e:
    print(e)