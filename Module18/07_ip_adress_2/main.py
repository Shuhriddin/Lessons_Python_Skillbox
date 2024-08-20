# TODO здесь писать код
print()
def correct_Ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

while True:
    ip = input('Введите IP: ')
    if correct_Ip(ip):
        print('IP-адрес корректен.')
    else:
        if len(ip.split('.')) != 4:
            print('Адрес — это четыре числа, разделённые точками.')
        else:
            for part in ip.split('.'):
                if not part.isdigit():
                    print(part, '— это не целое число.')
                elif int(part) < 0:
                    print(part, 'меншее 0')
                elif int(part) > 255:
                    print(part, 'превышает 255')
