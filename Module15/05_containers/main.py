# TODO здесь писать код
container = int(input('Количество контейнеров: '))
new_list = []

for i in range(container):
    container_weight = int(input('Введите вес контейнера: '))
    while container_weight > 200:
        print('Вес контейнера не должен перевышать 200')
        container_weight = int(input('Введите вес контейнера: '))
    new_list.append(container_weight)
new_weight = int(input('Введите вес нового контейнера: '))

while new_weight > 200:
    print('Вес контейнера не должен перевышать 200')
    container_weight = int(input('Введите вес контейнера: '))

index = 0
for i in range(len(new_list)):
    if new_list[i] <= new_weight:
        index = i + 1
        break
print('Номер, который получает новый контейнер:', index)