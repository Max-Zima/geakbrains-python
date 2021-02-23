class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Две клетки - хорошо, а одна большая - лучше! Размер клетки равен: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Клеточка стала меньше, теперь она равна: {sub} клеточкам' if sub > 0 else 'Клетка исчезла :('

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity // row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result

cell = Cell(int(input("Введите кол-во клеток: ")))
cell_2 = Cell(int(input("Введите кол-во клеток: ")))
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(int(input("Введите кол-во клеток в ряду: "))))