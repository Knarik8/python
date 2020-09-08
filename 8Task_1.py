"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        if self.day < 10:
            self.day = f"0{self.day}"
        if self.month < 10:
            self.month = f"0{self.month}"
        return (f"{self.day}-{self.month}-{self.year}")

    @classmethod #должен извлекать число, месяц, год и преобразовывать их тип к типу «Число»
    def int_1(cls, day, month, year):
        return cls(int(day), int(month), int(year))

    @staticmethod #ничего не знает о внутренней структуре класса
    def check(day, month, year):
        if (day > 31 or day < 1) or (month < 1 or month > 12) or (year < 1000 or year > 3000):
            print(f"Введена некорректная дата")

a = Date(5, 7, 2020)
print(a)
print(a.int_1(5, 7, 2020))
a.check(12, 78, 2020)
