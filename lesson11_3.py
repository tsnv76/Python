class CheckInt(Exception):
    def __init__(self, num):
        self.num = num


num_list = []
stoplist_num = ['Stop', 'stop']

try:
    while True:
        number = input('Введите целое число')
        if number.isdigit():
            num_list.append(number)
        elif number in stoplist_num:
            print(f'Твой список чисел {", ".join(num_list)}')
            raise CheckInt(f'Пользователь ввел {number}')
        else:
            print(f'Нужно ввести именно число!')
except CheckInt as e:
    print(f'Завершение работы: {e}')
