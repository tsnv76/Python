class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name}-> {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости у автомобиля {self.name}'
        else:
            return f'Скорость автомобиля {self.name} -> {self.speed}'

class PoliceCar(Car):
    pass

t_c = TownCar(50, 'Green', 'Bus', False)
s_c = SportCar(150, 'Red', 'Ferrari', False)
w_c = WorkCar(50, 'Red', 'Track', False)
p_c = PoliceCar(150, 'Red', 'PoliceCar', True)

print(p_c.show_speed())
print(t_c.go())
print(t_c.stop())
print(s_c.show_speed())
print(w_c.turn('на лево'))
print(w_c.show_speed())
print(p_c.show_speed())
print(s_c.show_speed())
