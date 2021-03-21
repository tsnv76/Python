from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def my_suit(self):
        print('Родительский метод для костюма')

    @abstractmethod
    def my_coat(self):
        print('Родительский метод для пальто')


class MyClothes(Clothes):
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def my_suit(self):
        quantity = 2 * self.h + 0.3
        print(f'Для пошива костюма нужно {quantity} м ткани')
        return quantity

    @property
    def my_coat(self):
        quantity = self.v / 6.5 + 0.6
        print(f'Для пошива пальто нужно {quantity:.2f} м ткани')
        return quantity


cloth = MyClothes(9, 1.75)
print(f'Для пошива пальто и костюма нужно {(cloth.my_suit + cloth.my_coat):.2f} м ткани')
