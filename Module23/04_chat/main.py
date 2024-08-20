# TODO здесь писать код
user_name = input("Как Вас зовут? ")
while True:
    print("1. Посмотреть текущий текст чата.\n2. Отправить сообщение.")
    response = input("Выберите действие: ")
    if response == '1':
        try:
            with open("chat.txt", 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print("Служебное сообщение пока ничего нет\n")
    elif response == '2':
        new_message = input("Введите сообщение: ")
        with open("chat.txt", 'a') as file:
            file.write('{name}: {message}\n'.format(
                name=user_name, message=new_message))
    else:
        print("Неизвестная команда\n")