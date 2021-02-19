from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_jokes = []

def get_jokes(n):
    """
    возвращающает n шуток, сформированных из двух случайных слов, взятых из трёх списков

    :param n: количество выводимых шуток
    :return: list of n jokes
    """
    for item in range(n):
            list_jokes.append(f'{choice(nouns).capitalize()} {choice(adverbs)} {choice(adjectives)}')

get_jokes(4)
print(list_jokes)
