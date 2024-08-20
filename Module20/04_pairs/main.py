# TODO здесь писать код
import random

# original_list = [random.randint(0, 100) for _ in range(10)]
# new_list = [(original_list[i], original_list[i+1]) for i in range(0, len(original_list), 2)]
#
# print("Оригинальный список:", original_list)
# print("Новый список:", new_list)

# 2-й СПОСОБ
original_list = [random.randint(0, 100) for _ in range(10)]
new_list = list(zip(original_list[::2], original_list[1::2]))

print("Оригинальный список:", original_list)
print("Новый список:", new_list)