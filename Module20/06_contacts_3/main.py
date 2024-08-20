# TODO здесь писать код
phone_dict = {}
while True:
    print()
    print('Введите номер действия:\n1.Добавить контакт.\n2.Найти человека.')
    action = input('При выборе действия: ')
    if action == '1':
        name_surname = input('Введите имя и фамилию нового контакта (через пробел): ')
        name, surname = name_surname.split()
        if (name, surname) in phone_dict:
            print('Такой человек уже есть в контактах.')
        else:
            phone_number = int(input('Введите номер телефона: '))
            phone_dict[(name, surname)] = phone_number
            print(f'Текущий словарь контактов: {phone_dict}')
    elif action == '2':
        search_surname = input('Введите фамилию для поиска: ')
        found = False
        for key, value in phone_dict.items():
            if search_surname.lower() in key[1].lower():
                print(' '.join(key), value)
                found = True
        if not found:
            print('Такого человека нет в контактах.')
    else:
        print('Ошибка!!! Введите правильную номер действия...')
