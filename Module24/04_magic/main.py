# TODO здесь писать код
class Water:
    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None


class Air:
    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None


class Fire:
    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Air):
            return Lightning()
        else:
            return None


class Earth:
    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None


class Storm:
    def __str__(self):
        return "Шторм"


class Steam:
    def __str__(self):
        return "Пар"


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()

result_storm = water + air
result_steam = water + fire
result_dirt = water + earth
result_lightning = air + fire
result_dust = air + earth
result_lava = fire + earth

print(f'{Water()} + {Air()} = {result_storm}')
print(f'{Water()} + {Fire()} = {result_steam}')
print(f'{Water()} + {Earth()} = {result_dirt}')
print(f'{Air()} + {Fire()} = {result_lightning}')
print(f'{Air()} + {Earth()} = {result_dust}')
print(f'{Fire()} + {Earth()} = {result_lava}')