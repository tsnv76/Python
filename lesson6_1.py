my_tuple = ()
my_list = []

with open('nginx_logs.txt', 'r') as f:
    for str_list in f:
        my_str = str_list.split('-')
        temp_str = my_str[2].split('"')
        _temp_str = temp_str[1].strip().split(' ')
        my_tuple = (my_str[0].strip(), _temp_str[0], _temp_str[1])
        my_list.append(my_tuple)

for num in my_list:
    print(f'{num}')
