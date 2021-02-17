my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for item in my_list:
    item_list = item.split(" ")
    name = item_list[-1].title()
    print(f'Привет, {name}!')
