import time
import multiprocessing
from fibonacci_original import fibonacci_recursive
from fibonacci_response import fibonacci_generator_n

TIMEOUT = 60  # секунди

def run_with_timeout(func, arg, timeout=TIMEOUT):
    def wrapper(queue):
        try:
            func(arg)
            queue.put("success")
        except Exception:
            queue.put("error")

    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=wrapper, args=(queue,))
    p.start()
    p.join(timeout)

    if p.is_alive():
        p.terminate()
        return "timeout"
    
    result = queue.get()
    return result

def benchmark(func, n_values):
    results = []
    for n in n_values:
        start = time.time()
        outcome = run_with_timeout(func, n)
        elapsed = time.time() - start if outcome == "success" else outcome
        results.append((n, f"{elapsed:.6f}" if isinstance(elapsed, float) else outcome))
        print("n =", results[-1])
    return results

def print_table(title, results):
    print(title)
    print("| n       | Time (s)  |")
    print("|---------|-----------|")
    for n, t in results:
        print(f"| {n:<7} | {t:<9} |")

# Значення для тесту
n_values = [5, 10, 20, 200, 500, 1000, 20000, 3000000]

# Бенчмарк
slow_results = benchmark(fibonacci_recursive, n_values)
fast_results = benchmark(fibonacci_generator_n, n_values)

# Таблиці
print_table("SLOW IMPLEMENTATION:", slow_results)
print()
print_table("FAST IMPLEMENTATION:", fast_results)
