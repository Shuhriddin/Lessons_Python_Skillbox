# TODO здесь писать код
import math

# Здесь создайте функцию get_sage_sqrt
def get_sage_sqrt(number):
    try:
        result = math.sqrt(number)
    except ValueError as exe:
        print(f"Ошибка: {exe}")
        result = None
    except TypeError as ece:
        print(f"Ошибка: {ece}")
        result = None
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        result = None
    return result


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")