guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

# TODO здесь писать код
while True:
    print()
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    action = input('Гость пришёл или ушёл? ')
    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break
    else:
        name_guests = input('Имя гостя: ')
        if action == 'пришёл':
            if len(guests) >= 6:
                print(f'Прости, {name_guests}, но мест нет.')
            else:
                guests.append(name_guests)
                print(f'Привет, {name_guests}')
        elif action == 'ушёл':
            if name_guests in guests:
                guests.remove(name_guests)
                print(f'Пока, {name_guests}!')
            else:
                print('Такого гостя нет на вечеринке!')
        else:
            print(f'{name_guests} не может уйти, его нет на вечеринке!')


