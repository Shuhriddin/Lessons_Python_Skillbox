# TODO здесь писать код
import os
from _collections_abc import Iterator

def gen_files_path(user_file: str, path=None) -> Iterator:
    if path is None:
        path = os.path.abspath(os.path.sep)
    print(f"Директопия поиска: {path}\n")
    for root, dirs, files in os.walk(path):
        print('\nПоиск идет в папках директории')
        for i_dir in dirs:
            yield os.path.join(root, i_dir)
        print('\nПоиск идет в файлах директории')
        for i_file in files:
            yield os.path.join(root, i_file)
        try:
            if user_file in dirs:
                return print(f'\nПапка {user_file} находится в директории')
            elif user_file in files:
                return print(f'\nФайл {user_file} находится в директории')
            raise FileNotFoundError(f'\nВ данной директории нет файла {user_file}')
        except FileNotFoundError as e:
            return print(e)

def main():
    name_file = 'main.py'
    for name in gen_files_path(name_file):
        print(name)
main()
