import sys

def odd_nums(n):
    for num in range(1, n, 2):
        yield num

n = 15
odd_to_n = odd_nums(n)
for i in odd_to_n:
    print(i)

next(odd_to_n)
