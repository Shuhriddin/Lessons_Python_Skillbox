nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

# TODO здесь писать код

def sort_list(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(sort_list(item))
        else:
            result.append(item)
    return result


finally_result = sort_list(nice_list)
print("Ответ:", finally_result)