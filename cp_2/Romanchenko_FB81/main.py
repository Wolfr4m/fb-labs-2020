import matplotlib.pyplot as plt
from collections import Counter
import re


def filter_text(l_text):
    l_text = re.sub("[^А-аЯ-я ]", "", l_text)
    l_text_with_spaces = l_text
    l_text_without_spaces = l_text.replace(" ", "")
    return l_text_with_spaces, l_text_without_spaces


def codable_things_of(alphabet):
    alphabet_length = len(alphabet)
    letter_index = {alphabet[key]: key for key in range(alphabet_length)}
    index_letter = {key: alphabet[key] for key in range(alphabet_length)}
    return letter_index, index_letter, alphabet_length


def encode_with_keys(l_text, alphabet):
    keys = ["ад", "рай", "ключ", "жесть", "оченьбольшоеслово"]
    encoded_texts = []
    for key in keys:
        encoded = encode(list(l_text), list(key), alphabet)
        encoded_texts.append(encoded)
    return encoded_texts, keys


def encode(l_text, l_key, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    key_len = len(l_key)
    for index in range(len(l_text)):
        l_text[index] = index_letter[(letter_index[l_text[index]] + letter_index[l_key[index % key_len]]) % alphabet_length]
    return "".join(l_text)


def decode(l_text, l_key, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    key_len = len(l_key)
    for index in range(len(l_text)):
        l_text[index] = index_letter[(letter_index[l_text[index]] - letter_index[l_key[index % key_len]]) % alphabet_length]
    return "".join(l_text)


def conformity_index(text):
    letter_amount = len(text)
    letter_and_amount = Counter(text)
    letter_and_amount = list(sorted(letter_and_amount.items(), key=lambda t: t[0]))
    i_c = 0
    for pair in letter_and_amount:
        i_c += (pair[1] * (pair[1] - 1)) / (letter_amount * (letter_amount - 1))
    return i_c


def draw_plot(key_lengths, i_cs):
    for index in range(len(key_lengths)):
        plt.bar(key_lengths[index], i_cs[index], width=0.8, bottom=None, align="center", data=None)

    plt.grid(which="major", color="r", linestyle="--", linewidth=0.1)
    plt.xlabel("Key length")
    plt.ylabel("Index of coincidence")
    plt.show()

def detect_possible_key_length(text, standart):
    candidates = []
    key_lengths = []
    i_cs = []
    for delta in range(2, 30):
        i_c = 0
        for j in range(0, delta):
            splited_text = ""
            for i in range(j, len(text), delta):
                splited_text += text[i]
            i_c += conformity_index(splited_text)
        i_c /= delta
        if standart - 0.005 < i_c < standart + 0.005:
            candidates.append((delta, i_c))
        i_cs.append(i_c)
        key_lengths.append(delta)
    # draw_plot(key_lengths, i_cs)
    return candidates


def bruteforce(text, possible_variants, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    possible_keys = []
    for possible_variant in possible_variants:
        key_length = possible_variant[0]
        print(text)
        print(key_length)

        for j in range(0, key_length):
            splited_text = ""
            for i in range(j, len(text), key_length):
                splited_text += text[i]
            print(j)
            print(splited_text)
            most_common_letter = Counter(splited_text).most_common(1)[0][0]
            print(most_common_letter)



    pass


russ_alphabet = list("абвгдежзийклмнопрстуфхцчшщъыьэюя")

# file = open("mytext.txt", "r", encoding="UTF-8")
# text = file.read().lower()
#
# print("\n" + str(text) + "\n")
# encoded, keys = encode_with_keys(text, russ_alphabet)
# for index in range(len(encoded)):
#     i_c = conformity_index(encoded[index])
#     print(f"Encoding text with {len(keys[index])} length key {keys[index]}" +
#           f" (text conformity index {i_c}): \n{encoded[index]}\n")



file = open("text.txt", "r", encoding="UTF-8")
text = file.read().lower()
print("\n" + text + "\n")

possible_variants = detect_possible_key_length(text, 0.055)
print("Candidates: \n" + str(possible_variants))

bruteforce(text, possible_variants, russ_alphabet)

