class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return self.cell + other.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            return "Error"
        elif self.cell > other.cell:
            return self.cell - other.cell

    def __mul__(self, other):
        return self.cell * other.cell

    def __floordiv__(self, other):
        if other.cell == 0:
            return "Делить на 0 нельзя"
        else:
            return self.cell // other.cell
    def make_order(self, rows):
        n = ""
        temp = self.cell
        count = round(self.cell // rows)
        while temp > 0:
            if temp >= count:
                n = n + "*" * count + "\n"
                temp = temp - count
            else:
                n = n + "*" * temp + "\n"

                temp = 0
        return n

a = Cell(15)
b = Cell(4)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a.make_order(2))



