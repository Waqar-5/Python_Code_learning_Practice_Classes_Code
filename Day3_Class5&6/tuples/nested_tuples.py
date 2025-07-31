# tuple_methods_and_nested_access.py
# 🌟 Mastering tuple methods and nested tuple access with real-life examples!

# -------------------------------
# 🔹 1. Basic Tuple Methods
# -------------------------------

# Tuples support a few built-in methods:
#   - .count(value): Counts how many times a value appears
#   - .index(value): Finds the first index of a value

fruit_tuple = ("apple", "banana", "apply", "cherry", "banana")

print("🔢 Count of 'apple': ", fruit_tuple.count("apple")) # output: 2
print("🔍 First index of 'banana': ", fruit_tuple.index("banana"))  # Output: 1



print("*****************************************")

student = ("Ali", ("Math", 85), ("Science", 90))
# Access name
print(student[0])             # Output: Ali

# Access subject names
print(student[1][0])          # Output: Math
print(student[2][0])          # Output: Science

# Access marks
print(student[1][1])          # Output: 85
print(student[2][1])          # Output: 90


print("******************************************")
trip = (
    ("Day 1", ("Karachi", "Hotel A")),
    ("Day 2", ("Lahore", "Hotel B")),
    ("Day 3", ("Islamabad", "Hotel C"))
)


# Access city of Day 2
print(trip[1][1][0])          # Output: Lahore

# Access hotel of Day 3
print(trip[2][1][1])          # Output: Hotel C

# Access whole Day 1 details
print(trip[0])                # Output: ('Day 1', ('Karachi', 'Hotel A'))

print("**************************************")
nested_numbers = (
    (1, 2),
    (3, 4, 5),
    ((6, 7), 8)
)

# Access 2
print(nested_numbers[0][1])   # Output: 2

# Access 5
print(nested_numbers[1][2])   # Output: 5

# Access 6
print(nested_numbers[2][0][0])  # Output: 6

# Multiply deeply nested 6 * 7 * 8
product = nested_numbers[2][0][0] * nested_numbers[2][0][1] * nested_numbers[2][1]
print(product)                # Output: 336


print("****************************************")
company = (
    ("IT", ("John", "Backend"), ("Emma", "Frontend")),
    ("HR", ("Ali", "Recruiter"), ("Sana", "Manager")),
)

# Access Emma's department and role
print(company[0][2][0])       # Output: Emma
print(company[0][2][1])       # Output: Frontend

# Access Ali's role
print(company[1][1][1])       # Output: Recruiter
