# TODO здесь писать код
def next_num(number):
    if number < 1:
        return 1
    if number >= 1:
        next_num(number-1)
        print(number)


number = int(input("Введите число: "))
next_num(number)