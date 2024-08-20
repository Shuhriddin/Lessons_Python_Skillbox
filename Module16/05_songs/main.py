violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

# TODO здесь писать код

while True:
    print()
    songs_count = int(input('Сколько песен выбрать? '))
    count = 0
    minute = 0
    for _ in range(songs_count):
        count += 1
        name_songs = input(f'Название {count}-й песни: ')
        for j_songs in violator_songs:
            if name_songs in j_songs:
                minute += j_songs[1]
                break
        else:
            print('Нет такой песни в списке')
    minute = round(minute, 2)
    print(f'Общее время звучания песен — {minute} минуты')




