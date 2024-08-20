# TODO здесь писать код
class Property:
    __worth = 0

    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def set_worth(self, worth):
        if worth > 0:
            return worth
        else:
            raise ValueError("Значение должно быть больше нуля")

    def get_worth(self):
        return self.__worth

    def tax(self):
        return self.__worth

class Apartment(Property):
    name = "Квартира"
    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return super().get_worth() / 1000

class Car(Property):
    name = "Машина"
    def __init__(self, worth):
        super().__init__(worth)
    def tax(self):
        return super().get_worth() / 200

class CountryHouse(Property):
    name = "Дача"
    def __init__(self, worth):
        super().__init__(worth)
    def tax(self):
        return super().get_worth() / 500

print("\nРасчет налога на имущество")
amount_money = int(input("Введите количество имеющихся денег: "))
summ_nalog = 0

worth_1 = float(input("Цена квартира: "))
worth_2 = float(input("Цена машина: "))
worth_3 = float(input("Цена дача: "))
tax_list = [Apartment(worth_1), Car(worth_2), CountryHouse(worth_3)]

for elem in tax_list:
    print("Налог на {} состоит {}".format(
        elem.name, elem.tax()
    ))
    summ_nalog += elem.tax()

print(f"\nСумма налога составила: {summ_nalog}")

if summ_nalog > amount_money:
    print(f"Вам не хватает, {summ_nalog - amount_money} для расчета с налоговой")
else:
    print(f"У вас получилось, осталось {amount_money - summ_nalog} наличных")