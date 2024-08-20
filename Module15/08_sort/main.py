# TODO здесь писать код
my_list = [1, 4, -3, 0, 10]
print(f'Изначальный список: {my_list}')
def buble_sort(number):
    for run in range(len(number)-1):
        for i in range(len(number)-1 - run):
            # print(f'сравниваем {n[i]} c {n[i+1]}')
            if number[i] > number[i+1]:
                number[i], number[i+1] = number[i+1], number[i]
    return number

print('Отсортированный список:', buble_sort(my_list))