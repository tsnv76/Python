class DivByZero(Exception):
    def __init__(self, divisor):
        self.div = divisor


try:
    divisible = float(input('Введите делимое >'))
    divisor = float(input('Введите делитель >'))
    if divisor != 0:
        print(f'Частное от деления {divisible} на {divisor} = {(divisible / divisor):.2f}')
    else:
        raise DivByZero(f'делить на 0 нельзя!')

except DivByZero as e:
    print(f'Ошибка {e}')
