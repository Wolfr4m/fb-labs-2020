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
    print(l_text)
    for key in keys:
        print(f"Encoding text with {len(key)} length key {key}")
        encoded = encode(list(l_text), list(key), alphabet)
        print(encoded)

def encode(l_text, l_key, alphabet):
    letter_index, index_letter, alphabet_length = codable_things_of(alphabet)
    key_len = len(l_key)
    for index in range(len(l_text)):
        l_text[index] = index_letter[(letter_index[l_text[index]] + letter_index[l_key[index % key_len]]) % alphabet_length]
    return "".join(l_text)

alphabet = list(" абвгдежзийклмнопрстуфхцчшщъыьэюя")

file = open("mytext.txt", "r", encoding="UTF-8")
text = file.read().lower()

encode_with_keys(text, alphabet)