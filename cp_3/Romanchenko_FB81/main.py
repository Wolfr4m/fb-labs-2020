from collections import *
import math


def codable_things_of(alphabet):
    alphabet_length = len(alphabet)
    letter_index = {alphabet[key]: key for key in range(alphabet_length)}
    index_letter = {key: alphabet[key] for key in range(alphabet_length)}
    return letter_index, index_letter


def gcd(first_num, second_num):
    if second_num == 0:
        return first_num
    else:
        return gcd(second_num, first_num % second_num)


def inverse(a, mod):
    for number in range(mod):
        if number * a % mod == 1:
            return number




def bigram_to_int(bigram, letter_index, alphabet_length):
    # print(f"{bigram} -> {letter_index[bigram[0]] * alphabet_length + letter_index[bigram[1]]} ")
    return letter_index[bigram[0]] * alphabet_length + letter_index[bigram[1]]


def int_to_bigram(integer, index_letter, alphabet_length):
    # print(f"{integer} -> {index_letter[(integer - integer % alphabet_length) / alphabet_length] + index_letter[integer % alphabet_length]} ")
    return index_letter[(integer - integer % alphabet_length) / alphabet_length] + index_letter[integer % alphabet_length]


def entropy(frequency_list, n_gram_lenght):
    entropy = 0
    for index in range(len(frequency_list)):
        entropy -= frequency_list[index][1] * math.log(frequency_list[index][1], 2)

    return entropy / n_gram_lenght


def frequency(elements):
    counter = OrderedDict(sorted(elements.items(), key=lambda kv: kv[1], reverse=True))
    frequency_list = []
    total_amount = sum(counter.values())
    for n_gram in counter:
        frequency_list.append((n_gram, counter[n_gram] / total_amount))
    return frequency_list


def find_keys(popular_text_bigrams, popular_lang_bigrams, alphabet):
    print(f"From lang: {popular_lang_bigrams}")
    print(f"From text: {popular_text_bigrams}")
    alphabet_length = len(alphabet)
    letter_index, _ = codable_things_of(alphabet)
    popular_text_bigrams = list(map(lambda x: bigram_to_int(x, letter_index, alphabet_length), popular_text_bigrams))
    popular_lang_bigrams = list(map(lambda x: bigram_to_int(x, letter_index, alphabet_length), popular_lang_bigrams))
    possible_keys = []
    mod = alphabet_length ** 2
    for pop_lan_big_ind1 in range(len(popular_lang_bigrams) - 1):
        for pop_lan_big_ind2 in range(pop_lan_big_ind1 + 1, len(popular_lang_bigrams)):

            for pop_text_big_ind1 in range(len(popular_text_bigrams)):
                for pop_text_big_ind2 in range(len(popular_text_bigrams)):
                    if pop_text_big_ind1 == pop_text_big_ind2:
                        continue
                    else:
                        Y1, Y2 = popular_text_bigrams[pop_text_big_ind1], popular_text_bigrams[pop_text_big_ind2]
                        X1, X2 = popular_lang_bigrams[pop_lan_big_ind1], popular_lang_bigrams[pop_lan_big_ind2]
                        print(f"{Y1} = a*{X1} + b mod {mod}")
                        print(f"{Y2} = a*{X2} + b mod {mod}")
                        print()
                        possible_keys.append([(pop_lan_big_ind1, pop_lan_big_ind2), (pop_text_big_ind1, pop_text_big_ind2)])
    print(len(possible_keys))
    return possible_keys


def brute(encoded_text, possible_keys):
    print(encoded_text)
    print(possible_keys)
    decoded_text = "kitty"
    return decoded_text

def hacking(encoded_text, alphabet):
    print(f"{alphabet}\n")
    # 2 means divide by non-crossed bigrams
    bigrammed_text = Counter([encoded_text[i:i + 2] for i in range(0, len(encoded_text), 2)])
    top_five_lang_bigrams = ["ст", "но", "то", "на", "ен"]
    top_five_text_bigrams, _ = map(list, zip(*frequency(bigrammed_text)[:5]))

    possible_keys = find_keys(top_five_text_bigrams, top_five_lang_bigrams, alphabet)

    decoded_text = brute(encoded_text, possible_keys)
    return decoded_text


rus_alphabet = "абвгдежзийклмнопрстуфхцчшщьыэюя"

file = open("17.txt", "r", encoding="UTF-8")
text = file.read().lower().replace("\n", "")
decoded = hacking(text, rus_alphabet)
print(decoded)

