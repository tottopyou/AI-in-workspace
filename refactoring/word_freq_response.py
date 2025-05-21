import re
import string
from collections import Counter

def most_common_words(filename, top_n=5):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = re.split(r'\s+', text)
    word_counts = Counter(filter(None, words))
    return word_counts.most_common(top_n)
