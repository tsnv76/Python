import random
my_list = []
numbers = 20
item = 0
print('Задание А')
while item < numbers:
    my_list.append(round(random.random() * 100, 2))
    rubl = int(my_list[item])
    int_kop = int(my_list[item] % 1 * 100)
    if int(int_kop) <10:
        kop = '0' + str(int_kop)
    else:
        kop = str(int_kop)
    print(f'{int(my_list[item])} рублей {kop}  копеек')
    item +=1
print('Задание B')

print("Первоначальный ID", id(my_list))
print(my_list)
my_list.sort()
print("ID после сортировки по возростанию", id(my_list))
print("Список после сортировки по возростанию", my_list)
print('Задание C')
my_list_reverse = sorted(my_list, reverse=True)
print("ID после сортировки по убыванию", id(my_list_reverse))
print("Список после сортировки по убыванию", my_list_reverse)
print('Задание D')
print(f'5 самых дорогих товара: {my_list_reverse[:5]}')