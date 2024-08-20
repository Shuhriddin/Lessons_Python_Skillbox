# TODO здесь писать код
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, max_depth=None):
    if max_depth is None or max_depth >= 1:
        if key in struct:
            return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, None if max_depth is None else max_depth - 1)
            if result:
                return result
    return None


user_key = input('Введите искомый ключ: ')
max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ")

if max_depth_input.lower() == "y":
    max_depth = int(input("Введите максимальную глубину: "))
else:
    max_depth = None

value = find_key(site, user_key, max_depth)
print('Значение ключа:', value)
