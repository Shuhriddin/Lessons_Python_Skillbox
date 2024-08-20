# TODO здесь писать код
text = input('Введите строку: ')
words = text.split()
big_string = ''
# count = 0
for word in words:
    if len(word) > len(big_string):
        big_string = word

print(f'Самое длинное слово: «{big_string}»')

count_word = len(big_string)
if count_word > 2:
    print(f'Длина этого слова: {count_word} символов')
else:
    print(f'Длина этого слова: {count_word} символ')
