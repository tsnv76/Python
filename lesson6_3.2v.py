from itertools import zip_longest

user_dic = {}

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
    user_dic = {name: line for name, line in zip_longest(f1.readlines(), f2.readlines(), fillvalue='None')}

print(user_dic)
