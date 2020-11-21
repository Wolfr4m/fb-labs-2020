from collections import Counter, OrderedDict
import re
import math


def filter_text(l_text):
    l_text = re.sub("[^А-аЯ-я ]", "", l_text)
    l_text_with_spaces = l_text
    l_text_without_spaces = l_text.replace(" ", "")
    return l_text_with_spaces, l_text_without_spaces


def frequency(counter, n_gram_lenght):
    counter = OrderedDict(sorted(counter.items(), key=lambda t: t[0]))
    frequency_list = []
    total_amount = sum(counter.values())
    for n_gram in counter:
        frequency_list.append((n_gram, counter[n_gram] / total_amount))

    entropy = 0
    for index in range(len(frequency_list)):
        entropy -= frequency_list[index][1] * math.log(frequency_list[index][1], 2)

    if int(n_gram_lenght) > 1:
        entropy /= n_gram_lenght
    return frequency_list, entropy, n_gram_lenght


def form_up_info(frequency_entropy_ngram, crossing, whitespaces):
    crossing = "" if crossing else "no-"
    whitespaces = "with" if crossing else "without"
    print(f"\nThe text divided as {frequency_entropy_ngram[2]}-grammed text with {crossing}crossing and {whitespaces} whitespaces ")
    for pair in frequency_entropy_ngram[0]:
        print(f"{pair[0]}-{str('%.5f' % pair[1])}")
    print("H =", str(frequency_entropy_ngram[1]))
    print("R =", str(1 - (frequency_entropy_ngram[1] / math.log(32, 2))) + "\n")


def text_info(l_text):
    text_with_spaces, text_without_spaces = filter_text(l_text)
    n = 2
    monogram_whitespaces = Counter(text_with_spaces)
    monogram_nowhitespaces = Counter(text_without_spaces)
    bigram_whitespaces_nocross = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n)])
    bigram_nowhitespaces_nocross = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n)])
    bigram_whitespaces_cross = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n - 1)])
    bigram_nowhitespaces_cross = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n - 1)])
    form_up_info(frequency(monogram_whitespaces, 1), False, True)
    form_up_info(frequency(monogram_nowhitespaces, 1), False, False)
    form_up_info(frequency(bigram_whitespaces_nocross, 2), False, True)
    form_up_info(frequency(bigram_nowhitespaces_nocross, 2), False, False)
    form_up_info(frequency(bigram_whitespaces_cross, 2), True, True)
    form_up_info(frequency(bigram_nowhitespaces_cross, 2), True, False)


file = open("text.txt", "r", encoding="UTF-8")
text = file.read().lower()
text_info(text)
