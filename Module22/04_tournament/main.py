# TODO здесь писать код

first_file = open('first_tour.txt', 'r', encoding='utf-8')
minimum_score = int(first_file.readline())  # read минимальный балл
name = []

for line in first_file:
    row = line.strip().split()
    if row[0].isalpha():
        name.append(row[1][0] + '.' + row[0] + ' ' + row[-1])  # append инициал, фамилия и баллов
first_file.close()  # обязательно закрыть файл после чтения

# фильтровать участников, прошедших во 2-ой тур
passed_to_second_tour = [entry for entry in name if int(entry.split()[-1]) > minimum_score]

# сортировка по фамилии изходя из баллов
sorted_data = sorted(passed_to_second_tour, key=lambda x: int(x.split()[-1]), reverse=True)

# записать в файл
answer_file = open('second_tour.txt', 'w', encoding='utf-8')
answer_file.write(str(len(sorted_data)) + '\n')  # количество всех участников 2-ого тура
count = 0
for entry in sorted_data:  # записать все участников
    count += 1
    answer_file.write(f'{count}) {entry} \n')
answer_file.close()