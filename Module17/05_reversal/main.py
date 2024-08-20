# TODO здесь писать код
text = input('Введите строку: ')

a = text[:text.find('h')]
b = text[text.find('h')+1:text.rfind('h')]
c = text[text.rfind('h')+1:]
reversed_sequence = a + b[::-1] + c
print('Развёрнутая последовательность между первым и последним h:', reversed_sequence)