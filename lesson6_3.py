import json

user_list = []
hobby_list = []
user_dic = {}

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobby.csv', 'r', encoding='utf-8') as f2:
    user_list = f1.readlines()
    hobby_list = f2.readlines()
    if len(user_list) < len(hobby_list):
        raise SystemExit(1)
    for num in range(len(user_list)):
        user_key = user_list[num].replace(', ', ' ').strip()
        if num >= len(hobby_list):
            user_dic[user_key] = 'None'
        else:
           user_dic[user_key] = hobby_list[num].strip()


print(f'Словарь до сохранения в файл               -> {user_dic}')
with open('user_info.txt', 'w', encoding='UTF-8') as f:
    json.dump(user_dic, f)

with open('user_info.txt', 'r', encoding='UTF-8') as f:
    user_dic = json.load(f)
print(f'Словарь после сохранения и чтения из файла -> {user_dic}')
