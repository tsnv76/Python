import os
from collections import defaultdict
from os.path import relpath
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
print(root_dir)
django_files = defaultdict(int)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        key_size = key_range(file_size)

        if file_size < key_size and file_size >= key_size // 10:
            django_files[key_size] += 1

for key_size, file_size in sorted(django_files.items(),
                         key=lambda x: x, reverse=False):
    print(f'{key_size}: {file_size}')
