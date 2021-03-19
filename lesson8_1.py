import re

RE_EMAIL = re.compile(r'\w[A-Za-z0-9-]+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}')
email_dic = {}
email_list = []
def email_parse(email):
    if not RE_EMAIL.match(email):
        msg = f'Неправильный адрес: {email}'
        raise ValueError(msg)
    else:
        email_list = email.split('@')
        key = email_list[0]
        email_dic[key] = email_list[1]
    return email_dic

email = input('Введите адрес: ')
email_parse(email)
print(email_dic)
