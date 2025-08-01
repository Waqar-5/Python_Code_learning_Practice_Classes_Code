# Unique Looping Concepts in Dictionaries
student = {"name": "Ali", "age": 20, "grade": "A"}

print("before apply loop: ", student)

for key in student:
    print(f"{key} → {student[key]}")

# for key, value in student.items():
#     print(f"{key} → {value}")


print("*************************************")
print("before apply loop: ", student)

#  Using .items() to Unpack Key–Value Pairs


for key, value in student.items():
    print(f"{key.upper()} = {value}")

print("*************************************")
# Loop With enumerate() for Index Tracking
print("before apply loop: ", student)

#  Adds serial numbers when printing dictionary contents.
for i, (key, value) in enumerate(student.items(), start=1):
    print(f"{i}. {key}: {value}")

print("***************************************")

print("before apply loop: ", student)

# Loop Over .values() Only
# Use when you're only interested in values, not keys.
for val in student.values():
    print(f"Value: {val}")

print("*****************************************")
print("before apply loop: ", student)

#  Loop to Reverse Key–Value Pairs
# ✅ Clever trick: Switch keys with values to create a new reversed dictionary.
reversed_dict = {}
for k, v in student.items():
    reversed_dict[v] = k

print("after apply or making reversed_dict: ",reversed_dict)

print("********************************************************")
students = {
    "Ali": {"Math": 85, "Science": 90},
    "Sara": {"Math": 92, "Science": 88}
}
print("before apply loop: ", students)
# Loop within a loop for nested dictionaries.
for name, subjects in students.items():
    print(f"📘 {name}'s Scores:")
    for subject, score in subjects.items():
        print(f" - {subject}: {score}")

print("****************************************************")

print("before apply loop: ", student)
# Filter Specific Items During Loop
# Use conditionals to handle only specific data types.
for key, value in student.items():
    if isinstance(value, int):
    # if isinstance(value, str):
        print(f"Numeric Field: {key} = {value}")

print("***************************************************")
# Loop to Count Frequencies
colors = ["red", "blue", "red", "green", "blue", "red"]
# colors = ["red","yellow", "blue", "blue", "blue", "red", "green", "blue", "red"]
frequency = {}
print("before apply loop: ", colors)


# ✅ Count occurrences using dict.get() inside a loop.
for color in colors:
    frequency[color] = frequency.get(color, 0) + 1

print(frequency)

print("**************************************************************")
# Building a Dictionary from Two Lists
keys = ["name", "age", "grade"]
values = ["Ali", 20, "A"]
print("keys:" , keys)
print("values:" , values)

#  Construct a dictionary using loops and two parallel lists.
data = {}
for i in range(len(keys)):
    data[keys[i]] = values[i]

print("After apply key value pairs: ",data)

print("*****************************************************")
# Sorting Dictionary in a Loop
marks = {"Ali": 88, "Sara": 95, "Omar": 78}
print("Original Dictionary: ", marks)

#  Sort and loop by values (highest first).
for name in sorted(marks, key=marks.get, reverse=True):
    print(f"{name}: {marks[name]}")
