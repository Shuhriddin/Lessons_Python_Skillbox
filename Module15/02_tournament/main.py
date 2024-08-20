# TODO здесь писать код

player_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
day_player = []
index = 1

for i in player_list:
    index += 1
    if index % 2 == 0:
        day_player.append(i)
print(f'Первый день: {day_player}')
