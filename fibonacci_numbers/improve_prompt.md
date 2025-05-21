
# ✅ User prompt: 

Я маю повільну функцію для обчислення чисел Фібоначчі:

```python
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

Цей код працює надто повільно для великих n. Можеш оптимізувати його, зберігши зрозумілу структуру? Я хотів би використовувати генератор або будь-який інший ефективний підхід.

---
# ✅ AI response

## `fibonacci_fast.py` — Оптимізований код на основі генератора
```python
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
```