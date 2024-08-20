# TODO здесь писать код
# Дано натуральное число n>1. Напишите функцию, которая находит его наименьший делитель, отличный от 1.

def findNumber(number):
    smallNum = 0
    for i in range(2, number + 1):
        if number % i == 0:
            smallNum = i
            break
    return smallNum


numbers = int(input('Введите число: '))
small = findNumber(numbers)

print(f'Наименьший делитель, отличный от единицы: {small}')
