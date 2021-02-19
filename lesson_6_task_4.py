class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет.\n'

    def stop(self):
        return f'{self.name} стоит.\n'

    def turn(self, direction):
        return f'{self.name} повернул на {direction}.\n'

    def show_speed(self):
        return f'Ваша скорость: {self.speed}\n'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы слишком быстро едете! Ваша скорсоть - {self.speed}'
        else:
            return f'Ваша скорость в норме ({self.name}км)'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы слишком быстро едете! Ваша скорсоть - {self.speed}'
        else:
            return f'Ваша скорость в норме ({self.name}км)'


class PoliceCar(Car):
    pass


town = TownCar(input("Введите название автомобился: "), int(input("Введите скорость автомобился: ")),
               input("Введите цвет автомобился: "), input("Введите значение is_police(True/False): "))
print('1:' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop() + '\n')

sport = SportCar(input("Введите название автомобился: "), int(input("Введите скорость автомобился: ")),
                 input("Введите цвет автомобился: "), input("Введите значение is_police(True/False): "))
print('2:' + sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop() + '\n')

work = WorkCar(input("Введите название автомобился: "), int(input("Введите скорость автомобился: ")),
               input("Введите цвет автомобился: "), input("Введите значение is_police(True/False): "))
print('3:' + work.go(), work.show_speed(), work.turn('право'), work.stop() + '\n')

police = PoliceCar(input("Введите название автомобился: "), int(input("Введите скорость автомобился: ")),
                   input("Введите цвет автомобился: "), input("Введите значение is_police(True/False): "))
print('4:' + police.go(), police.show_speed(), police.turn('право'), police.stop() + '\n')
