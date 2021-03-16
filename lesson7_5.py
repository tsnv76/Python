import os
from collections import defaultdict
import django

def key_range(item):
    count = 1
    while item > 0:
        count *= 10
        item //= 10
    if count == 1:
        count = 100
    return count

root_dir = django.__path__[0]

django_files = defaultdict(list)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        key_size = key_range(file_size)

        if file_size < key_size and file_size >= key_size // 10:
            if len(django_files[key_size]) == 0:
                django_files[key_size].append(0)
                django_files[key_size].append([])
                django_files[key_size][0] += 1
                ext = file.rsplit('.', maxsplit=1)[-1].lower()
                django_files[key_size][1].append(ext)
            else:
                django_files[key_size][0] += 1
                ext = file.rsplit('.', maxsplit=1)[-1].lower()
                django_files[key_size][1].append(ext)

file_name = 'summary.json'
with open(file_name, 'w', encoding='utf-8') as f:
    for keys in sorted(django_files, key=lambda x: x, reverse=False):
        f.write(f'{keys}: ({django_files[keys][0]}, {list(set(django_files[keys][1]))}\n')
        print(f'{keys}: ({django_files[keys][0]}, {list(set(django_files[keys][1]))}')
