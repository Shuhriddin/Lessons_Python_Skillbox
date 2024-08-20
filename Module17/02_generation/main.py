# TODO здесь писать код

number = int(input('Введите длину списка: '))

result = [1 if i % 2 == 0 or i == 0 else i % 5 for i in range(number)]
print(f'Результат: {result}')
