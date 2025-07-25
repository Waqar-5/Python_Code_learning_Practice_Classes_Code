# list_iteration_condition.py

# List of scores
scores = [55, 72, 81, 39, 67, 90]

# Categorize pass/fail using a loop with conditions

for score in scores:
    if score >= 60:
        print(f"{score} ✅ Pass")
    else:
        print(f"{score} ❌ Fail")


print("*****************************************")

# Filter passing scores into a new list
passing_scores = []
for s in scores:
    if s >= 60:
        passing_scores.append(s)

print("Passing Scores:", passing_scores)


print("*********************************************")

# While Loop, Nesting, and Advanced Methods
# Nested list of student records: [name, [math, science]]
records = [
    ["Ali", [75, 82]],
    ["Sara", [60, 58]],
    ["Bilal", [40, 45]]
]

# Loop with while
index = 0
while index < len(records):
    name, marks = records[index]
    avg = sum(marks) / len(marks)
    result = "✅ Pass" if avg >= 60 else "❌ Fail"
    print(f"{name} -> Avg: {avg:.1f} -> {result}")
    index += 1

# Use list comprehension to extract names of passed students
passed_students = [name for name, marks in records if sum(marks)/2 >= 60]
print("Passed Students:", passed_students)


print("*****************************************")

# for Loop with Lists
# Print all fruits in the list
fruits = ["apple", "banana", "mango", "cherry"]
for fruits in fruits:
    print(f"I love {fruits.title()}!")

print("******************************")

# Capitalize all names in a list
names = ["ahmed", "fatima", "bilal"]
print("Original list: ", names)
capitlized_name = []

for name in names:
    capitlized_name.append(name.capitalize())

print("Capitlized Names: ", capitlized_name)

print("*************************************")
numbers = [3, 7, 2, 8, 9, 12, 5]
print("Original list: ", numbers)
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print("Even Numbers: ", even_numbers)


print("**************************************")
print("Using while loop: ")
# while Loop with Lists 
tasks = ['learn python', 'make a portfolio', 'upload to GitHub']
print("origina tasks list: ", tasks)

while tasks:
    current_task = tasks.pop(0)
    print(f"Working on: {current_task}" )

# Move items from one list to another
print("***********************************")

unprocessed = ['image1', 'image2', 'image3']
print("Original unprocessed list: ", unprocessed)
processed = []

while unprocessed:
    item = unprocessed.pop()
    print(f"Processing: {item}")
    processed.append(item)

print("Done", processed)


print("******************************")
# Validate user input using a loop and list


valid_users = ['admin', 'moderator', 'editor']
print("Original valid_users: ", valid_users)
user = ''

while user not in valid_users:
    user = input("Enter a valid username: ")

print(f"Welcome, {user}!")


print("******************************")
# for Loop with enumerate()
colors = ['red', 'blue', 'green']
print("Original colors: ", colors)
for i, color in enumerate(colors):
    print(f"{i}: {color}")


print("*************************")
# Create numbered shopping list
shopping_list = ['milk', 'bread', 'eggs']
print("original shopting list: ", shopping_list)

for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")

print("*********************************")
# Replace an item based on position
numberlist = [10, 20, 30, 40]
print("Original number list: ", numberlist)
for i, val in enumerate(numberlist):
    if val == 30:
        numberlist[i] = 35

print("Updated List:", numberlist)

print("********************************")


users = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 25},
    {"name": "Zain", "age": 30}
]

for user in users:
    print(f"{user['name']} is {user['age']} years old.")

print("****************************")
# Looping over List of Dictionaries
users = [
    {"name": "Ali", "age": 22},
    {"name": "Sara", "age": 25},
    {"name": "Zain", "age": 30}
]

for user in users:
    print(f"{user['name']} is {user['age']} years old.")
