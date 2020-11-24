from collections import Counter, OrderedDict
import math


def codable_things_of(alphabet):
    alphabet_length = len(alphabet)
    letter_index = {alphabet[key]: key for key in range(alphabet_length)}
    index_letter = {key: alphabet[key] for key in range(alphabet_length)}
    return letter_index, index_letter


def entropy(frequency_list, n_gram_lenght):
    entropy = 0
    for index in range(len(frequency_list)):
        entropy -= frequency_list[index][1] * math.log(frequency_list[index][1], 2)

    if int(n_gram_lenght) > 1:
        entropy /= n_gram_lenght
    return entropy


def frequency(elements):
    counter = OrderedDict(sorted(elements.items(), key=lambda kv: kv[1], reverse=True))
    frequency_list = []
    total_amount = sum(counter.values())
    for n_gram in counter:
        frequency_list.append((n_gram, counter[n_gram] / total_amount))
    return frequency_list


def find_key(popular_text_bigrma, popular_lang_bigram):
    pass


def hacking(l_text, alphabet):
    print(alphabet)
    # 2 means divide by non-crossed bigrams
    bigrammed_text = Counter([l_text[i:i + 2] for i in range(0, len(l_text), 2)])
    frec = frequency(bigrammed_text)
    entr = entropy(frec, 2)
    print(frec)
    print(entr)


rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщьыэюя'

file = open("17.txt", "r", encoding="UTF-8")
text = file.read().lower().replace("\n", "")
hacking(text, rus_alphabet)
