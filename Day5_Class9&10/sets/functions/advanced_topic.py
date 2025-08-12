#  Functions are First-Class Citizens
# You can assign a function to a variable, pass it as an argument, or return it from another function.

def shout(msg): return msg.upper()
s = shout
print(s("hi"))  # HI


print("*************************************")
# 🔁 Functions Can Be Recursive by Nature
# Python has a default recursion limit (~1000).
# import sys
# sys.setrecursionlimit(2000)

# import sys
# sys.setrecursionlimit(2000)  # allow more recursive calls

# def test(n):
#     print(n)
#     test(n + 1)

# test(1)



print("*********************************")
# Closures (Functions Remembering State)
# Inner functions remember the variables from their outer scope even after the outer function ends.
def outer(x):
    def inner():
        print(x)
    return inner

f = outer(10)
f()  # prints 10 even though outer() has finished


print("***************************************")
#  Function Caching with functools.lru_cache
# Speeds up function calls by remembering previous results.
# from functools import lru_cache

from functools import lru_cache

@lru_cache(maxsize=None)
def square(x):
    print(f"Calculating square of {x}...")
    return x * x

print(square(4))  # Will calculate and print
print(square(4))  # Will use cache (faster, no print)

print("**********************************************")
# You Can Add Attributes to Function
def greet(): pass
greet.author = "Waqar"
print(greet.author)  # Waqar

print("**************************************")
#  The __name__ Attribute
# Every function has a special name attribute.
def fun(): pass
print(fun.__name__)  # fun

print("*************************************")
# Default Arguments Are Evaluated Once
# This causes mutability traps:
def add_item(item, mylist=[]):
    mylist.append(item)
    return mylist

# def add_item(item, mylist=None):
#     if mylist is None:
#         mylist = []


print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] – Not reset!


print("***************************************")
# Decorators Modify Function Behavior Without Changing It
def decorator(fn):
    def wrapper():
        print("Before")
        fn()
        print("After")
    return wrapper

@decorator
def hello(): print("Hello")
hello()


print("****************************************")
import timeit

# Function 1: using loop
def slow_function():
    result = 0
    for i in range(1000):
        result += i
    return result

# Run the timer
time_taken = timeit.timeit(slow_function, number=1000)
print("Time taken:", time_taken)


print("*********************************")
# Generators via yield
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)

print("*****************************************")
#  Functions in Lists/Dictionaries
def add(x, y): return x + y
def sub(x, y): return x - y

funcs = [add, sub]
print(funcs[0](5, 3))  # 8
print(funcs[1](5, 3))  # 2

print("************************************")
#  Callable Objects
class Hello:
    def __call__(self):
        print("Hello from object")

obj = Hello()
obj()  # behaves like a function

print("*****************************")
# Type Hints
def add(x: int, y: int) -> int:
    return x + y

print(add(2, 3))  # 5

print("****************************")
#  inspect Module
import inspect

def greet(name: str):
    return f"Hi {name}"

print(inspect.signature(greet))  # (name: str)

print("**********************************")

# Single Dispatch Function Overloading
from functools import singledispatch

@singledispatch
def process(data):
    print("General")

@process.register
def _(data: int):
    print("Integer")

@process.register
def _(data: str):
    print("String")

process(5)      # Integer
process("Hi")   # String

print("*********************************")
# Keyword-only Arguments
def display(*, name, age):
    print(name, age)

display(name="Ali", age=25)  # ✅ Must use keywords


print("************************************")
# __name__ and __doc__
def greet():
    """Say Hello"""
    return "Hello"

print(greet.__name__)  # greet
print(greet.__doc__)   # Say Hello

print("*********************************************")
# Renaming *args and **kwargs
def show(*values, **data):
    print(values)
    print(data)

show(1, 2, name="Waqar", age=25)

print("**************************************")
# ✅ Assign function to a variable
def greet():
    return "Hello!"

say_hi = greet  # assign function to variable
print(say_hi())  # → Hello!


print("************************************************************")
print("************************************************************")
print("************************************************************")
print("************************************************************")

# -----------------------------
# 1️⃣ Basic Function Definition
# -----------------------------
def greet():
    print("Hello, Python!")

greet()  # Hello, Python!

# -----------------------------
# 2️⃣ Function with Parameters
# -----------------------------
def welcome(name):
    print(f"Welcome, {name}!")

welcome("Waqar")  # Welcome, Waqar!

# -----------------------------
# 3️⃣ Function with Return Value
# -----------------------------
def add(a, b):
    return a + b

print(add(3, 7))  # 10

# -----------------------------
# 4️⃣ Default Parameter
# -----------------------------
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

say_hello()         # Hello, Guest!
say_hello("Sara")   # Hello, Sara!

# -----------------------------
# 5️⃣ Keyword Arguments
# -----------------------------
def student(name, grade):
    print(f"{name} got grade {grade}")

student(grade="A", name="Ali")

# -----------------------------
# 6️⃣ *args (Arbitrary Arguments)
# -----------------------------
def total(*numbers):
    print("Sum is:", sum(numbers))

total(1, 2, 3, 4)  # Sum is: 10

# -----------------------------
# 7️⃣ **kwargs (Keyword Arguments)
# -----------------------------
def profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

profile(name="Waqar", age=25, city="Karachi")

# -----------------------------
# 8️⃣ Lambda Function
# -----------------------------
square = lambda x: x * x
print(square(5))  # 25

# -----------------------------
# 9️⃣ Function Aliasing
# -----------------------------
def bye():
    print("Goodbye!")

farewell = bye
farewell()  # Goodbye!

# -----------------------------
# 🔟 First-Class Functions
# -----------------------------
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    return func("Hello")

print(speak(shout))   # HELLO
print(speak(whisper)) # hello

# -----------------------------
# 1️⃣1️⃣ Closures
# -----------------------------
def make_multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = make_multiplier(2)
print(double(5))  # 10

# -----------------------------
# 1️⃣2️⃣ Nested Functions
# -----------------------------
def outer():
    print("Outer Start")
    def inner():
        print("Inner Function")
    inner()
    print("Outer End")

outer()

# -----------------------------
# 1️⃣3️⃣ Function Attributes
# -----------------------------
def greet_user():
    return "Hi"

greet_user.author = "Waqar"
print(greet_user.author)  # Waqar

# -----------------------------
# 1️⃣4️⃣ __name__ and __doc__
# -----------------------------
def hello():
    """This function says hello"""
    return "Hello!"

print(hello.__name__)  # hello
print(hello.__doc__)   # This function says hello

# -----------------------------
# 1️⃣5️⃣ Docstring Access
# -----------------------------
def area(radius):
    """Calculates area of circle"""
    return 3.14 * radius * radius

print(area.__doc__)  # Calculates area of circle

# -----------------------------
# 1️⃣6️⃣ Mutable Default Argument Trap
# -----------------------------
def append_item(item, mylist=[]):
    mylist.append(item)
    return mylist

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2] ❗ shared list!

# ✅ Fix:
def safe_append(item, mylist=None):
    if mylist is None:
        mylist = []
    mylist.append(item)
    return mylist

print(safe_append(1))  # [1]
print(safe_append(2))  # [2]

# -----------------------------
# 1️⃣7️⃣ Recursive Function
# -----------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

# -----------------------------
# 1️⃣8️⃣ Function as Dictionary/List Value
# -----------------------------
def multiply(x, y): return x * y
def subtract(x, y): return x - y

operations = {
    "mul": multiply,
    "sub": subtract
}

print(operations["mul"](2, 3))  # 6

# -----------------------------
# 1️⃣9️⃣ Generators via yield
# -----------------------------
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(3):
    print(num)

# -----------------------------
# 2️⃣0️⃣ lru_cache – Memoization
# -----------------------------
from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # 55

# -----------------------------
# 2️⃣1️⃣ inspect.signature
# -----------------------------
import inspect

def show_info(name: str, age: int):
    pass

print(inspect.signature(show_info))  # (name: str, age: int)

# -----------------------------
# 2️⃣2️⃣ Callable Objects
# -----------------------------
class Greeter:
    def __call__(self):
        print("Hello from class!")

g = Greeter()
g()  # acts like a function

# -----------------------------
# 2️⃣3️⃣ Type Hints
# -----------------------------
def divide(x: float, y: float) -> float:
    return x / y

print(divide(10.0, 2.0))  # 5.0

# -----------------------------
# 2️⃣4️⃣ Keyword-only Arguments
# -----------------------------
def login(*, username, password):
    print(f"User: {username}")

login(username="admin", password="1234")  # ✅

# -----------------------------
# 2️⃣5️⃣ Single Dispatch Overloading
# -----------------------------
from functools import singledispatch

@singledispatch
def process(value):
    print("General")

@process.register
def _(value: int):
    print("Integer:", value)

@process.register
def _(value: str):
    print("String:", value)

process(10)      # Integer: 10
process("Hi")    # String: Hi
process([1, 2])  # General
