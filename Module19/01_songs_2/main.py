violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

# TODO здесь писать код

count_songs = int(input('Сколько песен выбрать? '))
minute = 0
for i_song in range(count_songs):
    name_song = input(f"Название {i_song+1} песни:: ")
    if name_song in violator_songs:
        minute += violator_songs[name_song]
    else:
        print('Такого песня нет в словарей')
print('Общее время звучания песен:', minute, 'минуты')
