# TODO здесь писать код
import random


class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def eat(self):
        self.satiety += 20
        self.house.food -= 10

    def work(self):
        self.satiety -= 10
        self.house.money += 50

    def play(self):
        self.satiety -= 10

    def go_shopping(self):
        self.house.food += 30
        self.house.money -= 30

    def live_day(self):
        dice = random.randint(1, 6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()


class House:
    def __init__(self):
        self.food = 50
        self.money = 0


house = House()
person1 = Person("Артём", house)
person2 = Person("Maria", house)

for day in range(365):
    person1.live_day()
    person2.live_day()

print("Окончательное состояние дома")
print("Еда:", house.food)
print("Деньги:", house.money)