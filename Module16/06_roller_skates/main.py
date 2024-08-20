# TODO здесь писать код

rolic = int(input('Количество роликов: '))
count = 0
rolic_list = []
for i in range(1, rolic + 1):
    size_path = int(input(f'Размер пары {i}: '))
    rolic_list.append(size_path)
# print(rolic_list)
print()

people = int(input('Количество людей: '))
people_list = []
for j in range(1, people + 1):

    foot_size = int(input(f'Размер ноги человека {j}: '))
    people_list.append(foot_size)
# print(people_list)

for num in people_list:
    for i in range(len(rolic_list)):
        if rolic_list[i] >= num:
            rolic_list.remove(rolic_list[i])
            count += 1
            break

print('\nНаибольшее количество людей, которые могут взять ролики:', count)