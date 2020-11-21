from collections import Counter
import re


def filter_text(l_text):
    l_text = re.sub("[^А-аЯ-я ]", "", l_text)
    l_text_with_spaces = l_text
    l_text_without_spaces = l_text.replace(" ", "")
    return l_text_with_spaces, l_text_without_spaces


def text_info(l_text):
    text_with_spaces, text_without_spaces = filter_text(l_text)

    n = 2
    monogram_whitespaces = Counter(text_with_spaces)
    monogram_nowhitespaces = Counter(text_without_spaces)
    bigram_whitespaces_nocross = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n)])
    bigram_nowhitespaces_nocross = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n)])
    bigram_whitespaces_cross = Counter([text_with_spaces[i:i + n] for i in range(0, len(text_with_spaces), n - 1)])
    bigram_nowhitespaces_cross = Counter([text_without_spaces[i:i + n] for i in range(0, len(text_without_spaces), n - 1)])
    print("Letter frequency with whitespaces:")
    print(monogram_whitespaces)
    print("Letter frequency without whitespaces:")
    print(monogram_nowhitespaces)
    print()
    print("Bigram frequency with whitespaces no crossing:")
    print(bigram_whitespaces_nocross)
    print("Bigram frequency without whitespaces no crossing:")
    print(bigram_nowhitespaces_nocross)
    print()
    print("Bigram frequency with whitespaces crossing:")
    print(bigram_whitespaces_cross)
    print("Bigram frequency without whitespaces crossing:")
    print(bigram_nowhitespaces_cross)
    pass


file = open("text.txt", "r", encoding="UTF-8")
text = file.read().lower()
text_info(text)
