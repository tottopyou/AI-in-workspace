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
