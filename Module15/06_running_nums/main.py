# TODO здесь писать код

numbers = [1, 2, 3, 4, 5]
steps = int(input('Сдвиг: '))
new_numbers = []

for i in numbers:
    new_numbers.append(i)

new_numbers = numbers[-steps:] + numbers[:-steps]
print(f'Изначальный список: {numbers}')
print('Сдвинутый список:', new_numbers)