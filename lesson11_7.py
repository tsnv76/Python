class Comlex:
    def __init__(self, complex_int, complex_img):
        self.complex_int = complex_int
        self.complex_img = complex_img

    def __str__(self):
        return f'({self.complex_int} + {self.complex_img}i)'

    def __add__(self, other):
        return Comlex(self.complex_int + other.complex_int, self.complex_img + other.complex_img)

    def __mul__(self, other):
        return Comlex(self.complex_int * other.complex_int - self.complex_img * other.complex_img,
                      self.complex_img * other.complex_int + self.complex_int * other.complex_img)


complex1 = Comlex(60, 10)
complex2 = Comlex(65, 11)
print(complex1)
print(complex2)
print(f'Сумма комплексных чисел {complex1 + complex2}')
print(f'Произведение комплексных чисел {complex1 * complex2}')
