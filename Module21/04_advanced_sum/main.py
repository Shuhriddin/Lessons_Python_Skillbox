# TODO здесь писать код
def summa(number):
    if isinstance(number, int):
        return number
    if isinstance(number, tuple):
        return sum(number)
    if isinstance(number, dict):
        return sum(number.values())
    if isinstance(number, list):
        result = 0
        for item in number:
            if isinstance(item, list):
                result += summa(item)
            else:
                result += item
        return result


print("Сумма Кортежа:", summa((1, 2, 3, 4, 5)))
print("Сумма Списки:", summa([[1, 2, [3]], [1], 3]))
print("Сумма Словарь:", summa({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))