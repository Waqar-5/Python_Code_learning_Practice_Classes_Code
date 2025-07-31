# nested_tuples.py
# 📘 Learn and play with Nested Tuples in Python with real-world examples and rich comments.

# ✅ What is a nested tuple?
# A nested tuple is a tuple inside another tuple.
# It helps organize complex data hierarchically and immutably.

# ------------------------------
# 🎓 Example 1: Student Database
# ------------------------------

students = (
    ("Alice", ("Math", 95), ("Science", 90)),
    ("Bob", ("Math", 88), ("Science", 82)),
    ("Charlie", ("Math", 75), ("Science", 78))
)

print("🎓 Student Grades:")
for student in students:
    name = student[0]
    math_grade = student[1][1]
    science_grade = student[2][1]
    print(f"  {name}: Math = {math_grade}, Science = {science_grade}")

print("****************************************************")
# ------------------------------
# 🍕 Example 2: Pizza Orders
# ------------------------------
pizza_orders = (
    ("Order001", ("Pepperoni", "Large", ("Cheese Burst", "Extra Olives"))),
    ("Order002", ("Veggie", "Medium", ("Thin Crust", "Jalapenos", "Mushrooms"))),
    ("Order003", ("BBQ Chicken", "Small", ("Stuffed Crust",)))
)

print("\n🍕 Pizza Orders:")
for order in pizza_orders:
    order_id = order[0]
    pizza_type = order[1][0]
    size = order[1][1]
    customizations = order[1][2]
    print(f"  {order_id}: {pizza_type} ({size}) with {', '.join(customizations)}")

# ------------------------------
# 🧳 Example 3: Travel Itinerary
# ------------------------------
trip = (
    ("Day 1", ("Karachi", "Hotel A")),
    ("Day 2", ("Lahore", "Hotel B")),
    ("Day 3", ("Islamabad", "Hotel C")),
)

print("\n🧳 Travel Itinerary:")
for day in trip:
    print(f"  {day[0]}: Visit {day[1][0]} and stay at {day[1][1]}")

# ------------------------------
# 🎲 Example 4: Nested Tuple Math
# ------------------------------
nested_numbers = (
    (1, 2),
    (3, 4, 5),
    ((6, 7), 8)
)

print("\n🎲 Nested Math Values:")
# Unpack and operate
a, b = nested_numbers[0]
print(f"  Sum of first tuple: {a + b}")

c, d, e = nested_numbers[1]
print(f"  Average of second tuple: {(c + d + e) / 3}")

(inner_tuple, x) = nested_numbers[2]
f, g = inner_tuple
print(f"  Product of deeply nested values: {f * g * x}")

# ------------------------------
# 🧠 Tips:
# - You CANNOT change a tuple, but you can read values with indexing or looping.
# - You can nest tuples as deeply as needed.
# - Use unpacking for clean access.

# ------------------------------
# 🧪 Practice: Try modifying this code to add a new student or pizza order.
# ------------------------------