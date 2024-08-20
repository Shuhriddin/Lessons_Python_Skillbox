# TODO здесь писать код
# Вариант 1
def polin(s):
    return s == s[::-1]

# Вариант 2
# def polin(s):
#     s1 = ''
#     for i in range(len(s)-1, -1, -1):
#         s1 += s[i]
#     return s == s1

while True:
    text = input('Введите слово: ')
    if polin(text) == True:
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')