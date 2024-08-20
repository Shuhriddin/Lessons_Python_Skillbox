# TODO здесь писать код
import random

out_file = "out_file.txt"

with open(out_file, 'w', encoding="utf-8") as file:
    pass

summ = 0
while summ < 777:
    try:
        number = int(input("Введите число: "))
        with open(out_file, "a") as file:
            file.write(str(number) + '\n')
        summ += number
        if random.randint(1, 13) == 1:
            raise Exception("Вас достигла неудача!")
    except ValueError:
        print("Ошибка: введите целое число")
    except Exception as e:
        print(e)
        break

if summ >= 777:
    print("Вы успешно выполнили условие для выхода из порочного цикла!")

with open(out_file, "r", encoding="utf-8") as file:
    print(f"Содержимое файла {out_file}:")
    for line in file:
        print(line.strip())