# Multiply Only Numbers

items = [3, "hello", 5, None, 2]

product = 1

for item in items:
    try:
        product *= item
    except TypeError:
        print(f"Skipping non-numeric value: {item}")

print("Product of all numbers:", product)
# Goal: Multiply all numbers, skip non-numeric items.


print("********************************************")

#  Count Valid Integers in a Mixed List

data = [100, "abc", 45, "xyz", 200, True]
count = 0

for value in data:
    try:
        if isinstance(value, int):
            count += 1
    except Exception:
        continue

print("Number of valid integers:", count)
# Goal: Only count items that are integers, safely.

print("****************************************")
#  Example 3: Safe Division with User Input
nums = [10, 0, 5, "x", 2]

for num in nums:
    try:
        result = 100 / num
        print(f"100 divided by  {num} is {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except TypeError:
        print(f"Invalid type for division: {num}")

# Goal: Show how try-except can handle multiple error types.

print("****************************************")


user_input = input("Enter a list of values separated by commas (e.g. 12, 1, a, 10, 2): ")

# Split the input into a list
items = user_input.split(",")

sumOfAllValues = 0
count = 0

for item in items:
    item = item.strip()  # Remove any extra spaces

    try:
        # Try converting to integer or float
        if '.' in item:
            number = float(item)
        else:
            number = int(item)

        sumOfAllValues += number
        count += 1

    except ValueError as e:
        print(f"Error converting '{item}': {e}")

# Calculate and print average
try:
    avg = sumOfAllValues / count
    print("Average of numeric values:", avg)
except ZeroDivisionError as e:
    print("No valid numbers entered. Cannot calculate average.")


"""
Part	Job Done
input()	Takes values from user
split()	Turns it into a list
try-except	Handles bad inputs (like letters)
float/int	Converts strings to numbers
sum + count	Tracks total and how many
average	Calculates safely
"""


print("***************************************************")
# ✅ Example 1: Add Only Positive Numbers
# 🎯 Goal: Ask user for values, ignore negatives, and calculate total sum.

user_input = input("Enter numbers (positive or negative), separated by commas: ")
items = user_input.split(",")

total = 0
skipped = []

for item in items:
    item = item.strip()
    try:
        number = float(item)
        if number >= 0:
            total += number
        else:
            skipped.append(number)
    except ValueError as e:
        print(f"Invalid input '{item}' - not a number.")

print("Sum of positive numbers:", total)
print("Skipped negative values:", skipped)

print("*********************************************************")

#  Example 2: Multiply All Valid Numbers
# 🎯 Goal: Multiply all valid numbers rom user input and show the product
user_input = input("Enter numbers separated by commas (e.g. 2, 3, x, 4): ")
items = user_input.split(",")

product = 1
valid_found = False

for item in items:
    item = item.strip()
    try:
        number = float(item)
        product *= number
        valid_found = True
    except ValueError as e:
        print(f"Skipping invalid item '{item}': {e}")

if valid_found:
    print("Product of all valid numbers:", product)
else:
    print("No valid numbers were entered.")    

print("****************************************************************")
# ✅ Example 3: Separate Strings and Numbers
# 🎯 Goal: Ask the user for a mixed list and divide it into strings vs numbers

user_input = input("Enter any values (numbers and words), separated by commas: ")
items = user_input.split(",")

numbers = []
words = []

for item in items:
    item = item.strip()
    try:
        num = float(item)
        numbers.append(num)
    except ValueError:
        words.append(item)

print("🟢 Numbers:", numbers)
print("🔵 Strings:", words)
