# TODO здесь писать код
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = input('Введите текст: ')

vowels_list = [i for i in text if i in vowels]
print(f'Список гласных букв: {vowels_list}')
count = len(vowels_list)
print(f'Длина списка: {count}')