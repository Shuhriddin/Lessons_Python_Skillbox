# TODO здесь писать код
from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == '__main__':
    result = list(map(lambda x, y: (x, y), letters, numbers))
    print(result)