# TODO здесь писать код
def circle_check(first_str, second_str):
    if len(first_str) != len(second_str):
        return False
    index = second_str.find(first_str[0])

    if index == -1:
        return False
    shifted = second_str[index:] + second_str[:index]

    if shifted == first_str:
        return True, index
    return False

first_text = input('Первая строка: ')
second_text = input('Вторая строка: ')
result = circle_check(first_text, second_text)

if result:
    print('Первая строка получается из второй со сдвигом', result[1])
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
