class Worker:
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] * self._income['bonus']


one_position = Position('Иванов', 'Иван', 'Manager', 3000, 1)
print(f'Полный доход сотрудника: {one_position.position} {one_position.get_full_name()} -> '
      f'{one_position.get_total_income()}')

two_position = Position('Сидоров', 'Василий', 'Supporter', 1000, 1.9)
print(f'Полный доход сотрудника: {two_position.position} {two_position.get_full_name()} -> '
      f'{two_position.get_total_income()}')
