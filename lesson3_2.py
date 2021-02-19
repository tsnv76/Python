my_words = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
            }

def num_translate_adv(my_str):
    if my_str.islower():
        print(my_words.get(my_str))
    else:
        print(my_words.get(my_str.lower()).capitalize())


one_str = str(input('Введите числительное от 0 до 10 на английском >'))
num_translate_adv(one_str)
