alphabet = 'abcdefg'

# TODO здесь писать код

again_alphabet = alphabet[:]

print('1', again_alphabet)              # abcdefg
print('2', again_alphabet[::-1])        # gfedcba
print('3', again_alphabet[::2])         # aceg
print('4', again_alphabet[1::2])        # bdf
print('5', again_alphabet[0:1])         # a
print('6', again_alphabet[-1])          # g
print('7', again_alphabet[3::5])        # d
print('8', again_alphabet[4:])          # efg
print('9', again_alphabet[3:5])         # de
print('10', again_alphabet[4:2:-1])     # ed