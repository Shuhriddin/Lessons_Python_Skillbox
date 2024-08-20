# TODO здесь писать код
def can_form_palindrome(s):
    sym_count = {}
    for sym in s:
        if sym in sym_count:
            sym_count[sym] += 1
        else:
            sym_count[sym] = 1

    odd_count = 0
    for count in sym_count.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


letter = input("Введите строку: ")
if can_form_palindrome(letter):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")