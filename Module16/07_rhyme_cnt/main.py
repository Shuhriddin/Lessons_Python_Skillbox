# TODO здесь писать код
persons = int(input('Количество человек: '))
my_list = []

for i in range(1, persons + 1):
    my_list.append(i)

calc = int(input('Какое число в считалке: '))
print(f'Значит, выбывает каждый {calc}-й человек')
print()

index = 0

while len(my_list) > 1:
    start_count = index % len(my_list)
    index = (index + calc - 1) % len(my_list)
    print(f'Текущий круг людей: {my_list}')
    print(f'Начало счёта с номера {my_list[start_count]}')
    print(f'Выбывает человек под номером {my_list[index]}')
    my_list.remove(my_list[index])
    print()
print(f'Остался человек под номером {my_list[0]}')