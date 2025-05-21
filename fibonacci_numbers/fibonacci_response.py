def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_generator_n(n):
    gen = fibonacci_generator()
    for _ in range(n):
        next(gen)
    return next(gen)

if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci_generator_n(i)}")