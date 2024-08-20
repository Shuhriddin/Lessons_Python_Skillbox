# TODO здесь писать код
# import math

count_video_cards = int(input('Количество видеокарт: '))
count = 0
new_list = []


for i in range(count_video_cards):
    count += 1
    video_cards = int(input(f'Видеокарта {count}: '))
    new_list.append(video_cards)
print(f'Старый список видеокарт: {new_list}', end='')

print('\nНовый список видеокарт: ', end='')

last_list = []
maximum = max(new_list)

for i in new_list:
    if i != maximum:
        last_list.append(i)
print(last_list)
