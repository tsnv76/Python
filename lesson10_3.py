class MyCell:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return f'Сумма клеток равна {self.num + other.num}'

    def __sub__(self, other):
        sub_cell = self.num - other.num
        if sub_cell >= 0:
            return f'Разность клеток равна {self.num - other.num}'
        else:
            return f'Разность клеток меньше 0'

    def __mul__(self, other):
        return f'Произведение клеток равно {self.num * other.num}'

    def __floordiv__(self, other):
        return f'Деление клеток равно {self.num // other.num}'


    def make_order(self, col):
        item = MyCell(self.num)
        str_cell = ''
        j = 1
        for i in range(item.num):
            str_cell += '*'
            if j == col:
                str_cell += '\n'
                j = 0
            j += 1
        return str_cell



cells1 = 20
cells2 = 20
cell1 = MyCell(cells1)
cell2 = MyCell(cells2)
print(f'Количество ячеек в одной клетке = {cells1}')
print(f'Количество ячеек во второй клетке = {cells2}')
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)

cells = 30
num_cell = 7
method_cell = MyCell(cells)
print(f'\nВсего {cells} клеток по {num_cell} клеток в ряду:')
print(method_cell.make_order(num_cell))
