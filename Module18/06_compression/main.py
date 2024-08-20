# TODO здесь писать код
print()

letter = input('Введите строку: ')
coded = []
count = 1
for i in range(len(letter)-1):
    if letter[i] == letter[i+1]:
        count += 1
    else:
        coded.append(letter[i] + str(count))
        count = 1
coded.append(letter[-1] + str(count))
result_coded = ''.join(coded)
print(f'Закодированная строка: {result_coded}')