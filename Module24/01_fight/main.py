# TODO здесь писать код
import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.score = 100

    def attack(self, enemy):
        enemy.score -= 20
        print(f'{self.name} атаковал, {enemy.name}. Здоровые {enemy.name}: {enemy.score}')


def score_war(warrior1, warrior2):
    while warrior1.score > 0 and warrior2.score > 0:
        attacker = random.choice([warrior1, warrior2])
        if attacker == warrior1:
            attacker.attack(warrior2)
        else:
            attacker.attack(warrior1)
    if warrior1.score <= 0:
        print(warrior2.name, "одержал победу!")
    else:
        print(warrior1.name, "одержал победу!")


warrior_1 = Warrior("Воин-1")
warrior_2 = Warrior("Воин-2")
score_war(warrior_1, warrior_2)