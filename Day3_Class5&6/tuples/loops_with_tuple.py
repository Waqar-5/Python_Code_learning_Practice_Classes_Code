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
    print("Found at index:", brands.index("Puma"))


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