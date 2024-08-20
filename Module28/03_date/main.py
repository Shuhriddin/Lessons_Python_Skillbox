# TODO здесь писать код
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        if cls.is_date_valid(date_str):
            return cls(day, month, year)
        else:
            raise ValueError("Invalid date format")

    @staticmethod
    def is_date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        if month in range(1, 13):
            if month == 2:
                if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                    return day in range(1, 30)
                else:
                    return day in range(1, 29)
            elif month in [4, 6, 9, 11]:
                return day in range(1, 31)
            else:
                return day in range(1, 32)
        return False

    def __str__(self):
        return f"День: {self.day}\tМесяц: {self.month}\tГод: {self.year}"


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))