# TODO здесь писать код
count_words = int(input('Введите количество пар слов: '))
words = {}
for i_word in range(count_words):
    key, value = input(f'{i_word+1}-я пара: ').split()
    words[key] = value
    words[value] = key


while True:
    user_word = input('Введите слово: ')
    if user_word in words:
        print(f'Синоним: {words[user_word]}')
        break
    else:
        print('Ошибка: такого слова нет. Попробуйте снова.')
