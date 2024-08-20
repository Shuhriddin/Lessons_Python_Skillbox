# TODO здесь писать код
def is_Prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number // 2) + 1):
        if number % i == 0:
            return False
    return True

def crypto(letter):
    return [element for i, element in enumerate(letter) if is_Prime(i)]


num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Ответ:', crypto(num))
print('Ответ:', crypto('О Дивный Новый мир!'))