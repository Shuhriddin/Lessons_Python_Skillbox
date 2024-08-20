# # TODO здесь писать код
# Напишите две функции. Первая принимает одно целое положительное число N
# и находит сумму всех цифр в числе. Вторая принимает число N и считает количество цифр в числе.
# В ответ выводится разность суммы чисел и количества.
def summ_number(number):
    num_summ = 0
    while number != 0:
        last_number = number % 10
        num_summ += last_number
        number //= 10
    return num_summ


def total_number(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count


user_number = int(input('Введите число: '))
summa = summ_number(user_number)
counter = total_number(user_number)
difference = summa - counter

print(f'Сумма чисел: {summa}')
print(f'Количество цифр в числе: {counter}')
print(f'Разность суммы и количества цифр: {difference}')