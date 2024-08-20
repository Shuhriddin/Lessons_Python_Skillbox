# TODO здесь писать код
import os
import os.path
# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.join('data', 'work_logs.txt')
output_file_path = os.path.join('data', 'output.txt')
# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/
# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/
def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

# Проверка наличия файлов
if os.path.exists(input_file_path) and not os.path.exists(output_file_path):
    with open(output_file_path, 'w') as output:
        for error_line in error_log_generator(input_file_path):
            output.write(error_line)
    print("Файл успешно обработан.")
else:
    print("Файлы не найдены или файл вывода уже существует.")