# TODO здесь писать код
print()

file_name = input('Название файла: ')

if not (file_name.endswith('.txt') or file_name.endswith('.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
elif file_name.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается недопустимым символом.')
else:
    print('Файл назван верно.')
