# TODO здесь писать код
print()
foods = 'утиное филе;фланк-стейк;банановый пирог;плов'
print(f'Доступное меню: {foods}.')
next_foods = foods.split(';')
# print(next_foods)
result_foods = ', '.join(next_foods)
print(f'Сейчас в меню есть: {result_foods}.')