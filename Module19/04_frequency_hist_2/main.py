# TODO здесь писать код
def count_sym(text):
    text_dict = dict()
    sym_count = 0
    for i_sym in text:
        if i_sym in text_dict:
            text_dict[i_sym] += 1
        else:
            text_dict[i_sym] = 1
    return text_dict

def invert_dict(original_dict):
    inverted_dict = dict()
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict


letter = input('Введите текст: ')
original_frequency_dict = count_sym(letter)
print('Оригинальный словарь частот:')
for j in original_frequency_dict:
    print(j, ':', original_frequency_dict[j])


inverted_frequency_dict = invert_dict(original_frequency_dict)
print('Инвертированный словарь частот:')
for i in inverted_frequency_dict:
    print(i, ':', inverted_frequency_dict[i])