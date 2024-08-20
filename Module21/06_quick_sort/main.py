# TODO здесь писать код

import random
def quick_sort(number):
    if len(number) > 1:
        x = number[random.randint(0, len(number)-1)]
        left = [i for i in number if i < x]
        center = [i for i in number if i == x]
        right = [i for i in number if i > x]
        number = quick_sort(left) + center + quick_sort(right)
    return number


new_list = [4, 9, 2, 7, 5]
result = quick_sort(new_list)
print(result)