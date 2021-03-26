class Data:
    def __init__(self, data_str):
        self.data_str = data_str

    @staticmethod
    def return_data(data_str):
        list_str = data_str.split('-')
        dd = int(list_str[0])
        mm = int(list_str[1])
        yy = int(list_str[2])
        return dd, mm, yy

    @classmethod
    def validation(cls, my_list):
        if my_list[0] > 31 or my_list[0] < 1 or my_list[1] > 12 or my_list[1] < 1:
            print(f'Дата введена неверно. Попробуйте еще раз или введите слово "Стоп"')
            return False
        else:
            print(f'Дата введена правильно.')
            return True


while True:
    data_str = str(input('Введите дату в виде строки день-месяц-год ->'))
    if data_str == 'Стоп' or data_str == 'Стоп':
        print('Пользователь ввел стоп-слово')
        break
    my_data = list(Data.return_data(data_str))
    flag = Data.validation(my_data)
    if flag:
        break
