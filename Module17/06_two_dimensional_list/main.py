# TODO здесь писать код
import random

first_list = [random.randint(1, 20) for i in range(3)]
second_list = [random.randint(1, 20) for j in range(3)]
three_list = [random.randint(1, 20) for r in range(3)]
four_list = [random.randint(1, 20) for x in range(3)]
last_list = [first_list[:], second_list[:], three_list[:], four_list[:]]
print(last_list)