import time
from word_freq_original import mostCommonWords as bad_version
from word_freq_response import most_common_words as good_version

def benchmark(func, filename, repeats=5):
    total_time = 0
    for _ in range(repeats):
        start = time.time()
        func(filename)
        total_time += time.time() - start
    return total_time / repeats

filename = "sample.txt"
bad_time = benchmark(bad_version, filename)
good_time = benchmark(good_version, filename)

print("| Version     | AVG time  (sec) |")
print("|------------|------------------------------|")
print(f"| Original     | {bad_time:.6f}                     |")
print(f"| AI refactored     | {good_time:.6f}                     |")
