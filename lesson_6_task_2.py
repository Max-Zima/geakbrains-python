class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__asphalt = 25
        self.__depth = 0.05

    def calc(self):
        return self._width * self._length * self.__asphalt * self.__depth / 10


print(f"{int(Road(length=int(input('Введите длину дороги: ')), width=int(input('Введите ширину дороги: '))).calc())}т")
