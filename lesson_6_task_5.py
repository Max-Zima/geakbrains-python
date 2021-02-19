class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'


class Pen(Stationary):

    def draw(self):
        return f'Запуск отрисовки {self.title} ручкой.'


class Pencil(Stationary):

    def draw(self):
        return f'Запуск отрисовки {self.title} карандашом.'


class Handle(Stationary):

    def draw(self):
        return f'Запуск отрисовки {self.title} маркером.'


pen = Pen(input("Что рисуется карандашом?"))
print(pen.draw())

pencil = Pencil(input("Что рисуется карандашом?"))
print(pencil.draw())

handle = Handle(input("Что рисуется карандашом?"))
print(handle.draw())
