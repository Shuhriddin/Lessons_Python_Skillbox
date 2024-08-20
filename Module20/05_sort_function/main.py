# TODO здесь писать код
# def tpl_sort(number):
#     number_list = list(number)
#     for run in range(len(number_list)-1):
#         for i in range(len(number_list)-1-run):
#             if number_list[i] > number_list[i+1]:
#                 number_list[i], number_list[i+1] = number_list[i+1], number_list[i]
#     return number_list

def tpl_sort(number):
    if all(isinstance(x, int) for x in number):
        return tuple(sorted(number))
    else:
        return number

tpl = (6, 3, -1, 8, 4, 10, -5)
print(f'Ответ: {tpl_sort(tpl)}')