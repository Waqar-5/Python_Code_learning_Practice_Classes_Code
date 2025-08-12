"""
it

🔹 Challenge 1: Add Only Even Numbers
✅ Goal:
Ask the user for a list of values. Add only even numbers and show the total.

🧠 Think about:
Convert each item to int

Check if number is even using % 2 == 0

Use try-except to handle non-numeric values
"""

mylist = [1, 2, 3, 4, 5]
even = []

for i in mylist:
    try:
        if i % 2 == 0:
            even.append(i)
    except TypeError as e:
        print(f"Error with value '{i}': {e}")

print("Even numbers:", even)


print("***********************************************")
user_input = input("Enter numbers separated by commas: ")
items = user_input.split(",")
even = []

for item in items:
    item = item.strip()
    try:
        num = int(item)
        if num % 2 == 0:
            even.append(num)
    except ValueError as e:
        print(f"Invalid input '{item}' — not a number.")

print("Even numbers are:", even)


print("******************************************************")


"""
🔹 Challenge 2: Count How Many Words and Numbers
✅ Goal:
User enters a mixed list like 12, hello, 4.5, world.
You should count:

How many numbers

How many words

🧠 Think about:
Try converting to float inside try

If it fails, count it as a word

🔍 Tip:
Use two counters: word_count, number_count
"""
user_input = input("Enter numbers and words separated by commas: ")
items = user_input.split(",")

# Create two variables to count numbers and words.
number_count = 0
word_count = 0


for item in items:
    item = item.strip()  # clean spaces
    try:
        number = float(item)  # works for both int and float
        number_count += 1
    except ValueError:
        word_count += 1
print("Number of numeric values:", number_count)
print("Number of words:", word_count)

print("******************************************************")

"""
🔹 Challenge 3: Divide 100 by Each Value
✅ Goal:
Ask user for values. Try to divide 100 / value and print each result.

🧠 Think about:
Handle ZeroDivisionError for 0

Handle ValueError for non-numbers

🔍 Tip:
Use try-except with multiple except blocks
"""
#  Step 1: Take Input
user_input = input("Enter a value: ")

# Split Input into a List
items = user_input.split(",")

# Loop Through Each Item
for item in items:
    item = item.strip()  # Remove extra spaces

# Use try-except to Divide 100 by Each Item
    try:
        number = float(item)
        result = 100 / number
        print(f"100 divided by {number} is {result}")

        # Catch Division or Conversion Errors
    except ZeroDivisionError:
        print(f"Cannot divide by zero: {item}")
    except ValueError:
        print(f"Invalid number: {item}")

print("*************************************")

"""
.

🔷 Challenge 4: Skip Numbers Greater Than 100
✅ Goal:
Ask user for numbers.

Add only numbers ≤ 100

Skip and show a message for values > 100 or invalid.


"""
user_input = input("Enter numbers separated by commas: ")
items = user_input.split(",")

total = 0

for item in items:
    item = item.strip()
    try:
        number = float(item)
        if number <= 100:
            total += number
        else:
            print(f"Skipped (greater than 100): {number}")
    except ValueError:
        print(f"Invalid input (not a number): {item}")

print("Sum of numbers less than or equal to 100:", total)


print("******************************************")
"""

🔷 Challenge 5: Average of Only Float Numbers
✅ Goal:
Ask user for values

Only keep float numbers (like 2.5, 3.14)

Ignore integers and strings

Calculate the average of floats


"""

user_input = input("Enter values (mix of floats, ints, words): ")
items = user_input.split(",")

float_sum = 0
float_count = 0

for item in items:
    item = item.strip()
    try:
        # Convert to float
        number = float(item)
        
        # Check if original item had a dot (float-like)
        if '.' in item:
            float_sum += number
            float_count += 1
        else:
            print(f"Skipped integer value: {item}")
    except ValueError:
        print(f"Invalid input: {item}")

# Calculate average
try:
    average = float_sum / float_count
    print("Average of float numbers:", average)
except ZeroDivisionError:
    print("No float numbers found.")

print("****************************************")
# Step 1: Get input from the user
user_input = input("Enter 5 values separated by commas: ")

# Step 2: Split input string into a list
items = user_input.split(",")

# Step 3: Loop through each item
print("Non-numeric values:")

for item in items:
    item = item.strip()  # Remove extra spaces

    try:
        # Try to convert to integer
        num = int(item)
        # If successful, it's a number — do nothing
    except ValueError:
        # If error, it's not a number — print it
        print(item)
