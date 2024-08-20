films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код
count_films = int(input('Сколько фильмов хотите добавить: '))
my_films = []

for i in range(count_films):
    name_film = input('Введите название фильма: ')
    if name_film in films:
        my_films.append(name_film)
    else:
        print(f'Ошибка: фильма {name_film} у нас нет :(')

print('Ваш список любимых фильмов:', ', '.join(my_films))