shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

# TODO здесь писать код
while True:
        name_details = input('Название детали: ')
        count = 0
        price = 0
        for detail in shop:
                if detail[0] == name_details:
                        count += 1
                        price += detail[1]
                else:
                        continue
        print(f'Количество деталей: {count}')
        print(f'Общая стоимость: {price}')
        print()