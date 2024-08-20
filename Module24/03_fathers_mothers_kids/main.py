# TODO здесь писать код
class Parents:
    def __init__(self, name, age, list_children):
        self.name = name
        self.age = age
        self.list_children = list_children

    def info(self):
        print(f'Меня зовут {self.name}. Мне {self.age} лет')

    def calmness(self, child):
        print(f'{self.name} успокаивает {child.name}')

    def feed_child(self, child):
        print(f'{self.name} кормит {child.name}')


class Child:
    def __init__(self, name, age, state_calm, state_hunger):
        if parent.age - age < 16:
            raise ValueError("Возраст ребёнка должен быть меньше возраста родителя хотя бы на 16 лет.")
        self.name = name
        self.age = age
        self.state_calm = state_calm
        self.state_hunger = state_hunger


# Создание экземпляров классов
parent = Parents("Иван", 40, ["Петя", "Вася"])
child1 = Child("Петя", 5, "спокойное", "голодное")
child2 = Child("Вася", 3, "возбужденное", "голодное")

# Вызов методов
parent.info()
parent.calmness(child1)
parent.feed_child(child2)