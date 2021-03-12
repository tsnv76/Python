import argparse

user_list = []
hobby_list = []
user_dic = {}

def save_file(in_file1, in_file2, out_file):

    with open(in_file1, encoding='utf-8') as f_u:
        len_file_user = sum(1 for l in f_u)
    with open(in_file1, encoding='utf-8') as f_u, open(in_file2, encoding='utf-8') as f_h, open(out_file, 'w', encoding='utf-8') as f_uh:
        for line in range(len_file_user):
            user_line = f_u.readline().strip('\n')
            hobby_line = f_h.readline().strip('\n')
            if hobby_line == '':
                hobby_line = 'None'
            f_uh.writelines([user_line, ': ', hobby_line, '\n'])


parser = argparse.ArgumentParser(description='Укажите имена файлов в виде: --f1="file1" --f2="file2" --f3="file3"')
parser.add_argument("--f1", default='users.csv', help="Значение по умолчанию - users.csv")
parser.add_argument("--f2", default='hobby.csv', help="Значение по умолчанию - hobby.csv")
parser.add_argument("--f3", default='users_hobby.txt', help="Значение по умолчанию - users_hobby.txt")
args = parser.parse_args()

save_file(args.f1, args.f2, args.f3)
