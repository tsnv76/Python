import sys

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Николай', 'Мария', 'Евгения']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

klass_tuple_list = ((tutors[num], klasses[num]) if num < len(klasses) else (tutors[num], 'None') for num in range(len(tutors)))

print(type(klass_tuple_list))
print(*klass_tuple_list)
