# 🧠 AI-Refactoring Demo: How ChatGPT Improves Code

This repository demonstrates how AI (e.g., ChatGPT) can refactor poorly written code into optimized, production-ready code. Each case includes:

- A **"bad" version** (original, naive implementation)
- An **"improved" version** (after ChatGPT refactoring)
- A **prompt file** used to request improvement
- A **benchmark** that visualizes the difference in performance

---

## 📘 Example 1: Fibonacci Number Generator

### 🔁 Task
Generate the `n`-th Fibonacci number.

### 📊 Benchmark Results

ORIGINAL IMPLEMENTATION:
| n       | Time (s)  |
|---------|-----------|
| 5       | 0.008644  |
| 10      | 0.001868  |
| 20      | 0.003185  |
| 200     | timeout   |
| 500     | timeout   |
| 1000    | error     |
| 20000   | error     |
| 3000000 | error     |

AI RESPONSE IMPLEMENTATION:
| n       | Time (s)  |
|---------|-----------|
| 5       | 0.002687  |
| 10      | 0.003490  |
| 20      | 0.004603  |
| 200     | 0.004251  |
| 500     | 0.002938  |
| 1000    | 0.004740  |
| 20000   | 0.008460  |
| 3000000 | 57.801419 |

### 🔗 Prompt File
See [fibonacci_numbers/improve_prompt.md](fibonacci_numbers/improve_prompt.md)

### ✅ Key Benefits from AI Refactor
- Eliminated recursion and exponential time complexity
- Replaced with memory-efficient `generator`
- Final solution is scalable and safe for large values of `n`

---

## 📘 Example 2: Word Frequency Counter

### 🔁 Task
Count the most frequent words in a `.txt` file.

### 📊 Benchmark Results

| Version     | AVG time  (sec) |
|------------|------------------------------|
| Original     | 0.001577                   |
| AI refactored     | 0.000110              |    

### 🔗 Prompt File
See [refactoring/improve_prompt.md](refactoring/improve_prompt.md)

### ✅ Key Benefits from AI Refactor
- Replaced unsafe file handling with `with open(...)`
- Used `str.translate` instead of inefficient `replace()` loops
- Applied `collections.Counter` for word counting
- Resulting code is faster, cleaner, and more Pythonic

---

## 🧠 Why This Matters

These examples clearly demonstrate that AI tools like ChatGPT can:
- Refactor and modernize legacy or naive code
- Improve performance (sometimes 10x–1000x)
- Suggest best practices and use standard libraries
- Save time for developers by offloading tedious rewrites

To replicate or adapt this approach:
1. Start with your raw code.
2. Write a clear **improvement prompt**.
3. Use ChatGPT or similar tools.
4. Benchmark the difference.

---
