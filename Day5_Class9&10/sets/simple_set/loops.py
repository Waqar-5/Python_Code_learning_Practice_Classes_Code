#  Looping Through Sets in Python
# Since sets are iterable, you can use loops to access each element one by one. This is useful for printing, filtering, or applying logic to every item.

# Basic for Loop on a Set
my_set = {10, 20, 30, 40}

for item in my_set:
    print("Item: ", item)
    #  Sets are unordered, so the printed order may vary each time you run it.

print("***************************************")

# Printing All Elements with Messages
names = {"Ali", "Asad", "Ameer"}

for name in names:
    print(f"Hello, {name}!")

print("*********************************")
# 2: Check for Even Numbers in Set
numbers = {11, 22, 33, 44, 55}

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    # else:
    #     print(f"{num} is odd")

print("************************************")
#  Counting Elements Manually
data = {1, 2, 3, 4, 5}
count = 0

for _ in data:
    count += 1

print("Total elements in set:", count)

print("**********************************")
# Add Elements to a New Set Based on Condition
original = {5, 10, 15, 20}
greater_than_10 = set()

for num in original:
    if num > 10:
        greater_than_10.add(num)

print("Filtered set:", greater_than_10) # {15, 20}

print("*****************************************")
# Nested Loop on Sets (Cartesian Product)
colors = {"red", "green"}
shapes = {"circle", "square"}

for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")

print("*********************************")
# RuntimeError (Modifying During Iteration)
my_set = {1, 2, 3}

for item in my_set:
    # ❌ Don't do this!
    # my_set.add(4)   # RuntimeError: Set changed size during iteration
    pass
