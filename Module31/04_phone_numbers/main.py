# TODO здесь писать код
import re


def check_phone_number(phone_number):
    if re.match(r'^[89]\d{9}$', phone_number):
        return "всё в порядке"
    else:
        return "не подходи"

numbers = ['9999999999', '999999-999', '99999x9999']

for key, value in enumerate(numbers):
    result = check_phone_number(value)
    print(f'{key + 1}: {result}')