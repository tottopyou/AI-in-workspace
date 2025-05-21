
# ✅ User prompt: 

У мене є код, який читає текстовий файл і повертає 5 найпоширеніших слів.
Він повільний, важко читається та має дублювання коду. Можеш переписати його:
- більш Pythonic;
- з використанням сучасних бібліотек (наприклад, Counter);
- без ручної очистки пунктуації;
- з хорошою структурою та читабельністю?

Ось мій код:
```python
def openFile(file):
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text

def remove_punctuation(text):
    for i in "!@#$%^&*()_+=-[]{};:'\",.<>?/|\\`~":
        text = text.replace(i, "")
    return text

def mostCommonWords(filename):
    data = openFile(filename)
    data = remove_punctuation(data)
    data = data.lower()
    words = data.split(" ")

    freq = {}
    for w in words:
        if w != "":
            if w in freq:
                freq[w] = freq[w] + 1
            else:
                freq[w] = 1

    freqList = []
    for k in freq:
        freqList.append([k, freq[k]])
    
    freqList.sort()
    return freqList[-5:]
```


---
# ✅ AI response

## `fibonacci_fast.py` — Оптимізований код на основі re
```python
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
```