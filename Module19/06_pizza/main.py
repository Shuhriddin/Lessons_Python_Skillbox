# TODO здесь писать код
number = int(input("Введите количество заказов: "))

orders = {}
for i in range(number):
    order = input(f"Заказ {i+1}: ").split()
    customer = order[0]
    pizza = order[1]
    quantity = int(order[2])
    if customer not in orders:
        orders[customer] = {}
    if pizza not in orders[customer]:
        orders[customer][pizza] = 0
    orders[customer][pizza] += quantity

for customer in sorted(orders.keys()):
    print(customer + ":")
    for pizza in sorted(orders[customer].keys()):
        print(f"{pizza}: {orders[customer][pizza]}")