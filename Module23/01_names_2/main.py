# TODO здесь писать код
sym_line = 0
count = 0

try:
    with open("people.txt", 'r', encoding='utf-8') as file:
        for line in file:
            count += 1
            length = len(line)
            if line.endswith('\n'):
                length -= 1
            if length < 3:
                print("Ошибка!!! менее трёх символов в строке", count)
                with open("errors.log", 'a', encoding='utf-8') as error_file:
                    error_file.write(f"Ошибка в строке {count}: {line}")
            sym_line += length
except FileNotFoundError:
    print("Файл не найден")
except BaseException as e:
    print("Произошло ошибка", e)
finally:
    print(f"Общее количество символов: {sym_line}.")