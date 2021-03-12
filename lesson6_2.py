my_tuple = ()
my_list = []

def most_frequent(list):
    dict = {}
    count, itm = 0, ''
    for item in reversed(list):
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return itm, count

with open('nginx_logs.txt', 'r') as f:
    for str_list in f:
        my_str = str_list.split('-')
        temp_str = my_str[2].split('"')
        _temp_str = temp_str[1].strip().split(' ')
        my_tuple = (my_str[0].strip(), _temp_str[0], _temp_str[1])
        my_list.append(my_tuple)

max_item, max_count = most_frequent([item[0] for item in my_list])

print(f'Спам идет с адреса -> {max_item}. \nКоличество запросов с него -> {max_count}')
