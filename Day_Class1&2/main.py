# Class 1 and 2 on python (Dated: 28/29-06-2025)



# Basic arithmetic

a = 10
b = 3

print("Addition:", a + b) # Output: 13
print("Subtraction:", a - b)  # Output: 7
print("Multiplication:", a * b)  # Output: 30
print("Division:", a / b)  # Output: 3.3333333333333335
print("Floor Division:", a // b)  # Output: 3
print("Modulus:", a % b)  # Output: 1
print("Exponentiation:", a ** b)  # Output: 1000



print("************************************")

# Flooring and Ceiling
import math
x = 3.3

print("Floor of 3.3: ", math.floor(x))  # Output: 3
print("Ceiling of 3.3: ", math.ceil(x))  # Output: 4


print("************************************")


# Boolean as Integers
# Boolean values can be used in math
print("True + True: ", True + True)  # Output: 2
print("True + False: ", True + False)  # Output: 1
print("False + False: ", False + False)  # Output: 0
print("True * 5: ", True * 5)  # Output: 5
print("False * 10: ", False + 10)  # Output: 10


print("************************************")

#  Logical Operators (AND, OR)
# AND = True only if both are True
print("True and True: ", True and True)  # Output: True
print("True and False: ", True and False)  # Output: False
print("False and False: ", False and False)  # Output: False

# OR = True if at least one is True
print("True or True: ", True or True)  # Output: True
print("True or False: ", True or False)  # Output: True
print("False or False: ", False or False)  # Output: False




print("************************************")

# Function Example with Parentheses

def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"
    # print(f"hello {name}!")  # This line will not execute because it's after the return statement
print(greet("Alice"))  # Output: Hello, Alice!


print("************************************")

#  String Concatenation
first_name = "Äli"
second_name = "Khan"
full_name = first_name + " " + second_name
print("Full Name:", full_name)  # Output: Full Name: Äli Khan



# Using f-string (modern & preferred)
age = 25
print(f"{full_name} is {age} years old.")  # Output: Äli Khan is 25 years old.


print("************************************")

# Input + Type Handling
user_input  = input("Enter any value: ")

print("Type before eval:", type(user_input))  # Output: <class 'str'>

try:
    evaluated = eval(user_input)
    print("Value after eval:", evaluated)
    print("Type after eval:", type(evaluated))  # Output: <class 'int'> or <

except:
    print("Not a valid Python expression. Still string.")


print("*************************************")

# Type Checking & type() vs JS-style typeof
# value = int(input("enter value: "))
value = 42  # Example value
print("Type of value:", type(value))  # Output: <class 'int'>

# Simulating JavaScript's typeof using a dictionary
def js_typeof(val):
    mapping = {
        str: "string",
        int: "number",
        float: "number",
        bool: "boolean",
        list: "array",
        dict: "object",
        tuple: "object",
        set: "object",
        type(None): "undefined",
    }
    return mapping.get(type(val), "object")
    
print("JavaScript-style typeof value:", js_typeof(value))  # Output: number



print("*************************************")
# Variables and IDE (Conceptual)
# Variables store data and are dynamic
language = "Python"
version = 3.11
print(f"{language} version is {version}")
