# TODO здесь писать код
import os
from collections.abc import Iterator

def gen_string_counter(directory: str) -> Iterator:
    for root, dirs, files in os.walk(directory):
        for file in files:
            count = 0
            if os.path.join(root, file).endswith('.py'):
                current_file = open(os.path.join(root, file), 'r', encoding="UTF-8")
                for line in current_file.readlines():
                    if not (line=='\n' or line.startswith(('"', '#', "'"))):
                        count += 1
                yield os.path.join(root, file), count

if __name__ == '__main__':
    for elem in gen_string_counter(directory='..'):
        print("Файл: {}, строка кода: {}".format(elem[0], elem[1]))