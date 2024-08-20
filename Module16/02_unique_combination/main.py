# TODO здесь писать код

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

for element in list2:
    if element not in list1:
        list1.append(element)
# print(list1)

def number_sort(number):
    for run in range(1, len(number) - 1):
        for i in range(1, len(number) - 1 - run):
            if number[i] > number[i+1]:
                number[i], number[i+1] = number[i+1], number[i]
    return number

last_list = number_sort(list1)
print(last_list)