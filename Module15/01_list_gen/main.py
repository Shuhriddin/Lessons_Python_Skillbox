# TODO здесь писать код

numbers = int(input('Введите число: '))
new_numbers = []

for i in range(numbers):
    if i % 2 == 1:
        new_numbers.append(i)
print(f'Список из нечётных чисел от одного до {numbers}: {new_numbers}')
