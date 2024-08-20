players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код

result = [keys + values for keys, values in players.items()]
print(f'Результат работы программы:\n{result}')
