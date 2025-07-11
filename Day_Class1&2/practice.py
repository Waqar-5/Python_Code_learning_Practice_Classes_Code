# 🧮 Python Calculator for All Operators (Dynamic Output)

# Step 1: Get input from the user
user_input1 = int(input("Enter first number: "))
user_input2 = int(input("Enter second number: "))

# Step 2: Perform all arithmetic operations and display results
print("\n🔢 Arithmetic Results:")

print(f"Addition (+):        {user_input1} + {user_input2} = {user_input1 + user_input2}")
print(f"Subtraction (-):     {user_input1} - {user_input2} = {user_input1 - user_input2}")
print(f"Multiplication (*):  {user_input1} * {user_input2} = {user_input1 * user_input2}")
print(f"Division (/):        {user_input1} / {user_input2} = {user_input1 / user_input2}")
print(f"Floor Division (//): {user_input1} // {user_input2} = {user_input1 // user_input2}")
print(f"Remainder (%):       {user_input1} % {user_input2} = {user_input1 % user_input2}")
print(f"Power (**):          {user_input1} ** {user_input2} = {user_input1 ** user_input2}")




print("*************************************")

print("\n📏 Smart Input Evaluator:")

# Step 1: Get input from the user
user_input = input("Enter a Python value (e.g., 3.14, True, 'text', [1,2], None): ")

# Step 2: Try to evaluate the input safely
try:
    evaluated_value = eval(user_input)
    print(f"✅ Value after eval: {evaluated_value}")
    print(f"📘 Type after eval: {type(evaluated_value)}")

    # Step 3: Optional Type Feedback
    if isinstance(evaluated_value, int):
        print("🔢 This is an integer.")
    elif isinstance(evaluated_value, float):
        print("🔬 This is a float.")
    elif isinstance(evaluated_value, bool):
        print("✅ This is a boolean.")
    elif isinstance(evaluated_value, str):
        print("📝 This is a string.")
    elif isinstance(evaluated_value, list):
        print("📚 This is a list.")
    elif isinstance(evaluated_value, dict):
        print("🗂️ This is a dictionary.")
    elif isinstance(evaluated_value, tuple):
        print("🧺 This is a tuple.")
    elif evaluated_value is None:
        print("🚫 This is a NoneType.")
    else:
        print("❓ Unrecognized type.")

except Exception as e:
    print(f"⚠️ Invalid input or unsafe expression: {e}")
    print("🔁 Treating as string:")
    print(f"Input: {user_input}")
    print(f"Type: {type(user_input)}")



print("*************************************")


# Boolean Logic Testing

# True is treated as 1, False as 0 in arithmetic
print("\n🔍 Boolean Logic Testing:")
print("True + False :", True + False) # Output: 1
print("True * 10: ", True * 10) # Output: 10
print("False + 100: ", False +  100) # Output: 10




print("*************************************")


# JavaScript-Style typeof() Function in Python

def js_typeof(value):
    """
    Simulates JavaScript's typeof in Python.
    """
    type_map = {
        str: "string",
        int: "number",
        float: "number",
        bool: "boolean",
        list: "object",
        dict: "object",
        tuple: "object",
        type(None): "undefined"
    }

    return type_map.get(type(value), "object")  # fallback = "object"


# 🧪 Test the function with different types
print("\n🧪 Testing js_typeof:")

print("js_typeof('hello')      →", js_typeof("hello"))       # string
print("js_typeof(123)          →", js_typeof(123))           # number
print("js_typeof(3.14)         →", js_typeof(3.14))          # number
print("js_typeof(True)         →", js_typeof(True))          # boolean
print("js_typeof([1, 2, 3])    →", js_typeof([1, 2, 3]))      # object
print("js_typeof({'a': 1})     →", js_typeof({"a": 1}))       # object
print("js_typeof((1, 2))       →", js_typeof((1, 2)))         # object
print("js_typeof(None)         →", js_typeof(None))           # undefined
print("js_typeof(set([1,2]))   →", js_typeof(set([1,2])))     # object (fallback)


print("*************************************")
# String Concatenation and Formatting

user_name1 = input("Enter your name: ")
user_age = input("Enter your age: ")

print("\n➕ Using + for Concatenation:")
print("My name is" + user_name1 + "and I am " + user_age + "years old.")


print("\n🧵 Using f-string (simple):")
print("f-string Method: \n",f"My name is {user_name1} and I am {user_age} years old.")  # Using f-string for better readability

print("\n🔠 Using f-string with .upper():")
print("f-string Method: \n",f"My name is {user_name1.upper()} and I am {user_age} years old.")  # Using f-string for better readability

print("\n⭐️ Using f-string with .title():")
print("f-string Method: \n",f"My name is {user_name1.lower()} and I am {user_age} years old.")  # Using f-string for better readability


print("\n📏 Length of your name:")
print(f"Your name has {len(user_name1)} characters.")

print("*************************************")



# 🧪 Part 6: Functions and Parentheses Practice

# Functions and Parenthesis Practice
def welcom(name):
    """
    Function to welcome a user by name.
    """
    # print(f"Hello, {name}! Wlcome to Python Courses.")
    print(f"Hello, {name.title()}! Welcome to Python Courses.")  # .title() capitalizes name properly

# Call the function with a name
welcom("Asad")  # Output: Hello, Asad! Welcome to Python Courses.
welcom("Ali")  # Output: Hello, Ali! Welcome to Python Courses.
welcom("Muneer")  # Output: Hello, Muneer! Welcome to Python Courses.


print("*************************************")

# Floor and Ceil Practice
import math

user_input_floor = float(input("Enter a number to find its floor value: "))

print(f"Floored value: {user_input_floor} is: {math.floor(user_input_floor)}")  # Using math.floor for floor value
print(f"Ceiled value: {user_input_floor} is: {math.ceil(user_input_floor)}")  # Using math.ceil for ceil value


# Build a Mini CLI App: