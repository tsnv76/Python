import sys
my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(my_list)
my_list2 = []
for item in my_list:
    if item.isnumeric() and len(item) == 2:
        my_list2.extend(['"', item, '" '])
    elif item.isnumeric() and int(item) < 10:
        my_list2.extend(['"', '0' + item, '" '])
    elif item[0] == '+':
        my_list2.extend(['"', item[0] + '0' + item[-1], '" '])
    else:
        my_list2.extend([item," "])
print(my_list2)
my_str=''.join(my_list2)
print(my_str.capitalize())
