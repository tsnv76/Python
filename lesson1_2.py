N = 1000
odd_numbers = []
number = 0
summ_number_list = 0
while number < N:
    if number % 2:
        odd_numbers.append(number ** 3)
    number += 1
for idx in odd_numbers:
    _sum = 0
    num = idx
    while (num != 0):
        _sum = _sum + num % 10
        num = num // 10
    if not _sum % 7:
        summ_number_list += idx
print('Сумма чисел= ', summ_number_list)
summ_number_list = 0
for idx in range(len(odd_numbers)):
    odd_numbers[idx] += 17
    _sum = 0
    num = odd_numbers[idx]
    while (num != 0):
        _sum = _sum + num % 10
        num = num // 10
    if not _sum % 7:
        summ_number_list += odd_numbers[idx]
print('Сумма чисел с изменением= ', summ_number_list)
