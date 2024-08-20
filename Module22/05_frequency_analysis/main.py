# TODO здесь писать код
alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

text = open('text.txt', 'r').read().lower()
dict_letter = {}
count = 0
for i_letter in text:
    if i_letter in alfabet:
        x = dict_letter.get(i_letter, 0)
        dict_letter[i_letter] = x + 1
        count += 1

sort_dict = sorted(dict_letter)
result = [[i_elem, round((dict_letter[i_elem] / count), 3)] for i_elem in sort_dict]
analysis = '\n'.join([i_elem[0] + ' ' + str(i_elem[1]) for i_elem in result])

finally_part = open('analysis.txt', 'w')
finally_part.write(analysis)