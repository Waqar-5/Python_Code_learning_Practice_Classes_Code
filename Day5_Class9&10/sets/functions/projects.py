# Fibonacci with Recursion, Caching, and Benchmarking
import timeit                          # ⏱️ Used to measure function execution time
from functools import lru_cache        # 🧠 Used to cache function calls

# 🌀 Define a recursive Fibonacci function with caching
@lru_cache(maxsize=None)               # 🎯 Remembers results to avoid re-computation
def fibonacci(n):
    if n <= 1:
        return n                      # 🔙 Base case
    return fibonacci(n-1) + fibonacci(n-2)  # 🔁 Recursive case

# ▶️ Main function to run and test
def run_fibonacci():
    num = 30                          # 📌 Test value
    print(f"Fibonacci of {num} is: {fibonacci(num)}")

    # 🧪 Measure time taken to compute fibonacci
    execution_time = timeit.timeit(lambda: fibonacci(num), number=1)
    print(f"Execution time with cache: {execution_time:.5f} seconds")

run_fibonacci()


print("*********************************************")
# Speak Function with Decorator & Nested Function
# 🎤 A decorator that takes another function and applies it
def speak(func):                             # 💬 `func` is a function passed as input
    def wrapper():                           # 🔁 Wrapper adds extra behavior
        result = func("Hello")               # 🗣️ Call the passed function
        print(result)                        # 🖨️ Print its result
    return wrapper                           # ⏪ Return the wrapped function

# 🔊 Normal function to make text loud
def shout(text):
    return text.upper() + "!!!"              # 💥 Convert to uppercase

# 🤫 Function to make text quiet
def whisper(text):
    return text.lower() + "..."              # 📉 Convert to lowercase

# 🧪 Use decorator manually
decorated_shout = speak(shout)               # 📎 Apply `speak` to `shout`
decorated_whisper = speak(whisper)           # 📎 Apply `speak` to `whisper`

decorated_shout()                            # 🔊 Output: HELLO!!!
decorated_whisper()                          # 🤫 Output: hello...


print("**********************************")
# Calculator with Nested, Lambda, and Dynamic Functions
# ➗ Calculator that takes a function as input
def calculator(operation, x, y):             # 🧮 Takes a function and two numbers
    return operation(x, y)                   # 🔁 Call passed function with numbers

# ➕ Define basic math operations using lambda
add = lambda a, b: a + b                     # ➕ Add function
subtract = lambda a, b: a - b                # ➖ Subtract function
multiply = lambda a, b: a * b                # ✖️ Multiply function
divide = lambda a, b: a / b if b != 0 else "Error"  # ➗ Divide with zero check

# 🧪 Try calculator with different functions
print
