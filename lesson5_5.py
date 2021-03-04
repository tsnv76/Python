import sys
from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


start = perf_counter()
result = [num for num in src if (src.count(num) == 1)]
print(f'         Обычный результат -> {result}. Время выполнения {(perf_counter() - start)}')


start = perf_counter()
uniq_src = set()
tmp = set()
for el in src:
    if el not in tmp:
        uniq_src.add(el)
    else:
        uniq_src.discard(el)
    tmp.add(el)
result1 = [el for el in src if el in uniq_src]
print(f'Оптимизированный результат -> {result1}. Время выполнения {(perf_counter() - start)}')
