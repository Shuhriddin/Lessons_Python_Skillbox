# TODO здесь писать код
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Задача 1
# Без использования множеств
commond_elements = []

for element in array_1:
    if element in array_2 and element in array_3:
        commond_elements.append(element)
print("Задача 1:")
print("Решение без множеств:", end=" ")
for i in commond_elements:
    print(i, end=" ")

# С использованием множеств
set_array_1 = set(array_1)
set_array_2 = set(array_2)
set_array_3 = set(array_3)
commond_element_set = list(set_array_1.intersection(set_array_2, set_array_3))
print("\nРешение с множествами:", end=" ")
for i in commond_element_set:
    print(i, end=" ")

# Задача 2
# Без использования множеств
unique_list = []
for num in array_1:
    if num not in array_2 and num not in array_3:
        unique_list.append(num)

print("\n\nЗадача 2:")
print("Решение без множеств:", end=" ")
for i in unique_list:
    print(i, end=" ")

# С использованием множеств
unique_elements_set = list(set_array_1.difference(set_array_2, set_array_3))
print("\nРешение с множествами:", end=" ")
for i in unique_elements_set:
    print(i, end=" ")