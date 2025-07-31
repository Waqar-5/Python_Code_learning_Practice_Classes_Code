# Tuple + Loops
# Looping Through Tuple Using for

fruits = ("apple", "banana", "cherry")
print("original tuple: ", fruits)
for fruit in fruits:
    print(f"Fruits: {fruit}")

print("*****************************")
#  Using enumerate() with Tuple
colors = ("red", "blue", "green")
for index, color in enumerate(colors):
    print(f"Index {index} => {colors}")

print("***************************8")

# Using While Loop with Tuple
numbers = (5, 10, 15, 20)
print("original tuple:", numbers)
i = 0
while i < len(numbers):
    print(f"Value at {i}: {numbers[i]}")
    i += 1

print("*************************")
# Tuple Iteration with Condition
marks = (40, 85, 67, 90, 55)
print("Original tuple: ", marks)
for mark in marks:
    if mark >= 60:
        print(f"{mark} is Pass")
    else:
        print(f"{mark} is Fail")

print("*****************************")
# Tuple + Conditions
# Check Membership with if

animals = ("cat", "dog", "cow")
print("original tuple: ", animals)
if "dog" in animals:
    print("Dog is found")

print("***************************************")
# Count and Compare
nums = (1, 1, 2, 3, 1)
if nums.count(1) > 2:
    print("1 appears more than twice")

print("***********************************")
#  Index Lookup and Action
brands = ("Nike", "Adidas", "puma")
print("Original tuple: ", brands)
if "puma" in brands:
    # print("Found at index:", brands.index("Puma")) show valueerror because case senstive
    print("Found at index:", brands.index("puma"))
else:
    print("not found")

print("*************************************")
# Condition with Slicing
t = (10, 20, 30, 40, 50)
print("Original tuple: ", t)
if sum(t[1:4]) > 60:
    print("Middle slice sum is large")

print("**************************************")

nums = (1, 2, 2, 3, 2)
if nums.count(2) == 3:
    print("2 occurs 3 times")

print("*******************************************")
status = ("ok", "fail", "ok", "ok")
print("ok:", status.count("ok"))


print("************************************")
empty = ()
print(empty.count("anything"))  # 0
print("*************************************")

grades = ("A", "B", "C", "A")
print("First A is at", grades.index("A"))

print("***************************************")
cities = ("Paris", "London", "New York", "Paris")
if "Paris" in cities:
    print(cities.index("Paris"))

print("********************************")
t = (5, 6, 7, 8)
if 7 in t:
    i = t.index(7)
    print("Found at:", i)

print("**************************************")
students = (
    ("Ali", ("Math", 85), ("Science", 90)),
    ("Sara", ("Math", 92), ("Science", 88)),
    ("Zara", ("Math", 78), ("Science", 80))
)


print("🎓 Student Grades (with indexing):")
for student in students:
    name = student[0]
    math_score = student[1][1]
    science_score = student[2][1]
    print(f"{name}: Math = {math_score}, Science = {science_score}")


print("*******************************************")
print("\n📦 Student Grades (with unpacking):")
for name, (sub1, mark1), (sub2, mark2) in students:
    print(f"{name}: {sub1} = {mark1}, {sub2} = {mark2}")


print("*********************************************")
print("\n🔢 Access using index range:")
for i in range(len(students)):
    name = students[i][0]
    math_score = students[i][1][1]
    science_score = students[i][2][1]
    print(f"{name}: Math = {math_score}, Science = {science_score}")
print("*****************************************************")
pizza_orders = (
    ("Order001", ("Pepperoni", "Large", ("Cheese Burst", "Extra Olives"))),
    ("Order002", ("Veggie", "Medium", ("Thin Crust", "Mushrooms"))),
)

print("\n🍕 Pizza Orders:")
for order_id, (flavor, size, customizations) in pizza_orders:
    print(f"{order_id}: {flavor} ({size}) with {', '.join(customizations)}")

print("*********************************************")
students = (
    ("Ali", ("Math", 85), ("Science", 90)),
    ("Sara", ("Math", 92), ("Science", 88, ("ali", "khan", "meer"))),
)
print("🎓 Student Records with Deep Nesting:")
for student in students:
    name = student[0]
    math_score = student[1][1]
    
    # Handle nested structure of Science tuple
    science_data = student[2]
    science_score = science_data[1]
    
    # Check if bonus info is present
    if len(science_data) > 2:
        bonus_names = science_data[2]
        print(f"{name}: Math = {math_score}, Science = {science_score}, Extra = {', '.join(bonus_names)}")
    else:
        print(f"{name}: Math = {math_score}, Science = {science_score}")
