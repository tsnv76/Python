import os
list_file = []

file_name = 'config.yaml'
with open(file_name, 'r') as f:
    for line in f:
        list_file.append(line.split(','))

full_path = ''
root = ''
sub_dir = ''
sub_sub_dir = ''
sub_sub_sub_dir = ''
sub_sub_sub_sub_dir = ''
flag = True

for item in list_file:
    if len(item[0]) == 1:
        root = item[1].strip()
        sub_dir = ''
    if len(item[0]) == 2:
        sub_dir = f'\{item[1].strip()}'
        sub_sub_dir = ''
        sub_sub_sub_dir = ''
        sub_sub_sub_sub_dir = ''
    if len(item[0]) == 3:
        sub_sub_dir = f'\{item[1].strip()}'
        sub_sub_sub_dir = ''
        sub_sub_sub_sub_dir = ''
    if len(item[0]) == 4:
        sub_sub_sub_dir = f'\{item[1].strip()}'
        sub_sub_sub_sub_dir = ''
    if len(item[0]) == 5:
        sub_sub_sub_sub_dir = f'\{item[1].strip()}'

    full_path = f'{root}{sub_dir}{sub_sub_dir}{sub_sub_sub_dir}{sub_sub_sub_sub_dir}'

    if full_path.endswith('.py') or full_path.endswith('.html'):
        with open(full_path, 'w', encoding='utf-8') as f:
            print()
    else:
        if not os.path.exists(full_path):
            os.mkdir(full_path)
    full_path = ''
    flag = True
