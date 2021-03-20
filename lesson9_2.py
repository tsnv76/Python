import time


class Road:
    __length = 1
    __width = 1

    def __init__(self):
        self.__length = 20
        self.__width = 5000

    def calc_mass(self, weight, width_1_m):
        print(f'{self.__length}м * {self.__width}м * {weight}кг * {width_1_m}см = {(self.__length * self.__width * weight * width_1_m) // 1000} т.')


r = Road()
print(r.calc_mass(25, 5))
