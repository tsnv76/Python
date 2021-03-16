import os
list_file = []

file_name = 'starter.txt'
with open(file_name, 'r') as f:
    for line in f:
        list_file.append(line.split(','))

full_path = ''
root = ''
sub_dir = ''
sub_sub_dir = ''

for item in list_file:
    if len(item[0])  == 1:
       root = item[1].strip()
    if len(item[0]) == 2:
        sub_dir = f'\{item[1].strip()}'
    if len(item[0]) == 3:
        sub_sub_dir = f'\{item[1].strip()}'
    full_path = f'{root}{sub_dir}{sub_sub_dir}'
    try:
        if not os.path.isdir(item[1].strip()):
            os.mkdir(full_path)
    except FileExistsError:
        print(f'Файл {full_path} существует')
    full_path = ''
    sub_sub_dir = ''
