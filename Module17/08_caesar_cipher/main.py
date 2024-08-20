# TODO здесь писать код
def caesar_cipher(string, user_shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)] if sym in alphabet else sym) for sym in string]
    new_str = ''.join(char_list)
    return new_str

input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)
print('Зашифрованная строка:', output_str)
