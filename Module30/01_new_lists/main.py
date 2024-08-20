# TODO здесь писать код
from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

if __name__ == '__main__':
    print("*" * 50)
    result_floats = list(map(lambda x: round((x ** 3), 3), floats))
    print("floats возводится в третью степень и округляется до трёх знаков\n", result_floats)

    print("*" * 50)
    result_names = list(filter(lambda x: len(x) >= 5, names))
    print("Имена минимум из пяти букв:\n", result_names)

    print("*" * 50)
    result_numbers = reduce(lambda x, y: x*y, numbers)
    print("Произведение всех чисел:\n", result_numbers)