# TODO здесь писать код
print()
password = input('Придумайте пароль: ')

while (len(password) < 8 or
       sum(number.isdigit() for number in password) < 3 or
       not any(letter.isupper() for letter in password)):
    password = input('Пароль ненадёжный. Попробуйте ещё раз. \nПридумайте пароль: ')
print('Это надёжный пароль.')