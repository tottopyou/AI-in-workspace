def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci_recursive(i)}")
