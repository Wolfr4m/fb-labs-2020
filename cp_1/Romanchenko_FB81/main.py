from collections import Counter
import re

def filter_text(text):
    text = re.sub("[^А-аЯ-я ]", "", text)
    text_with_spaces = text
    text_without_spaces = text.replace(" ", "")
    return text_with_spaces, text_without_spaces

file = open("text.txt", "r", encoding="UTF-8")
text = file.read().lower()

lol, kek = filter_text(text)

print(kek)
