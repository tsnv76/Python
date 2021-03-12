import json

user_list = []
hobby_list = []
user_dic = {}

with open('users.csv', encoding='utf-8') as f_u:
    len_file_user = sum(1 for l in f_u)

with open('users.csv', encoding='utf-8') as f_u, open('hobby.csv', encoding='utf-8') as f_h, open('users_hobby.txt', 'w', encoding='utf-8') as f_uh:
    for line in range(len_file_user):
        user_line = f_u.readline().strip('\n')
        hobby_line = f_h.readline().strip('\n')
        if hobby_line == '':
            hobby_line = 'None'

        f_uh.writelines([user_line, ': ', hobby_line, '\n'])
