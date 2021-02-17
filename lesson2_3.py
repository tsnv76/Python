import sys
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list, id(my_list))
for item in my_list:
    str_element = ''
    if item.isnumeric() and len(item) == 2:
        str_element = item
        my_list.insert(my_list.index(item) + 1, '" ')
    elif item.isnumeric() and int(item) < 10:
        str_element = '0' + item[-1]
        my_list.insert(my_list.index(item) + 1, '" ')
    elif item[0] == '+':
        str_element = item[0] + '0' + item[-1]

        my_list.insert(my_list.index(item) + 1, '" ')
    else:
        str_element = item + ' '
    my_list[my_list.index(item)] = str_element
print(my_list, id(my_list))

my_str=''.join(my_list)
print(my_str.capitalize())
