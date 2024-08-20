# TODO здесь писать код
# 1-способ
number = int(input("Введите число: "))
class SquareNumbers:
    def __init__(self, number: int) -> None:
        self.number = number
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.number:
            self.current += 1
            return self.current ** 2
        else:
            raise StopIteration

square_nums = SquareNumbers(number)

print("Квадрат чисел с используя класса: ", end='')
for i in square_nums:
    print(i, end=' ')
print()

# 2-способ
def square_numbers(number):
    for num in range(1, number+1):
        yield num ** 2

print("Квадрат чисел с используя генератор функцию: ", end=' ')
result = square_numbers(number)
for s in result:
    print(s, end=' ')
print()

# 3-способ
print("Квадрат чисел с используя генератора выражения: ", end=' ')
nums = (i**2 for i in range(1, number+1))
for j in nums:
    print(j, end=' ')