import sys

n = 25
odd_to_n = (num for num in range(1, n, 2))

for i in odd_to_n:
    print(i)

next(odd_to_n)
