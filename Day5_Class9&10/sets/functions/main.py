#  Basic Syntax of a Function

# def function_name(parameters):
#     # code block
#     return value


"""
def — keyword to define a function.

function_name — name of the function (follows variable naming rules).

parameters — optional input values (also called arguments).

: — colon to start the function block.

return — optional; used to return a value from the function.
"""

def greet():
    print("Hello, welcome to Python!")

greet()

print("********************************************")

# Default Parameters
def greet(name = "Friend"):
    print("Hello", name)

greet()   # Hello Friend
greet("Khan") # Hello Khan

print("***************************************")

# Function Definition with Default Parameters:
def greet(name="Guest", message="Welcome!"):
    print(f"Hello {name}, {message}")

# Calling with Positional Arguments (using default parameters):
greet()                  # Positional: uses both default values
# Output: Hello Guest, Welcome!

greet("Waqar")           # Positional: overrides `name`, keeps default `message`
# Output: Hello Waqar, Welcome!

greet("Ali", "Hi!")      # Positional: overrides both `name` and `message`
# Output: Hello Ali, Hi!

print("****************************************")
# Keyword Arguments
def student(name, age):
    print(f"{name} is {age} years old")

student(age= 18, name="Waqar")

print("****************************************")
# . *Arbitrary Arguments (args)
def add_numbers(*args):
    total = sum(args)
    return total

print(add_numbers(1, 2, 3, 4)) # Output: 10


print("**************************************")
#  **Arbitrary Keyword Arguments (kwargs)
def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

info(name = "Waqar", age=19, city = "Larkana", education = "12th Pass!")

print("*****************************************")
# Docstring (Documentation for Functions)
def greet():
    """This function greets the user"""
    print("Hello!")

print(greet.__doc__)

print("**********************************")

# Function Scope: Local vs Global Variables
x = 10  # global

def my_func():
    x = 5  # local
    print("Inside:", x)

my_func()
print("Outside:", x)


print("**********************************")
# Lambda (Anonymous) Functions
# square = lambda x: x * x
# print(square(5)) # output: 25
square = lambda x, y: x ** y
print(square(5, 2)) # output: 25

print("***************************************")
# Nested Functions
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()


print("************************************")
# 🔊 Function that takes a string and returns it in uppercase
def shout(text):
    return text.upper()  # Convert text to UPPERCASE

# 🤫 Function that takes a string and returns it in lowercase
def whisper(text):
    return text.lower()  # Convert text to lowercase

# 🗣️ Higher-order function: accepts another function as an argument
def speak(func):
    result = func("Hello")  # Call the passed-in function with the argument "Hello"
    print(result)           # Print the result of that function

"""
def speak(func):                  # Define a function named speak that takes another function as input
    result = func("Hello")        # Call that function using the word "Hello" and store the result
    print(result)                 # Show the result on the screen

"""


# 📢 Calling `speak()` with the `shout` function as an argument
speak(shout)    # Output: HELLO

# 🤐 Calling `speak()` with the `whisper` function as an argument
speak(whisper)  # Output: hello


print("**********************************")
# Recursive Functions 
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # output: 120