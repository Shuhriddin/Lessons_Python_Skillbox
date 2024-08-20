# TODO здесь писать код
summa = 0
number_file = open('numbers.txt', 'r', encoding='utf-8')
for i_line in number_file:
    columns = i_line.strip()
    if columns:
        summa += int(columns)
number_file.close()

answer_file = open('answer.txt', 'w', encoding='utf-8')
answer_file.write(str(summa))
answer_file.close()