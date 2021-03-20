class Stationery:
    title = 'Мелом'

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки маркером'


st = Stationery()
pen = Pen()
pencil = Pencil()
handle = Handle()

print(st.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())


