# ✅ 1. append() – Adds a single element at the end of the list
# Example 1: Add one student name to class list

students = ["Ali", "Sara"]
students.append("Hamza")
print(students) # ['Ali', 'Sara', 'Hamza']


# Example 2: Add number to marks list using condition
marks = [45, 67, 88]
if 100 not in marks:
    marks.append(100)
print(marks)

# Example 3: Append inside a loop

new_names = []
for i in range(3):
    name = input("Enter name: ")
    new_names.append(name)
print("All names:", new_names)

print("********************************************")
# insert(index, element) – Insert item at specific position
# Example 1
colors = ['red', 'blue']
colors.insert(1, 'green')
print(colors)  # ['red', 'green', 'blue']
# Example 2: Insert only if index is valid
index = 2
if index <= len(colors):
    colors.insert(index, 'yellow')
print(colors)

# Example 3: Use loop to insert numbers at beginning
nums = []
for i in range(3):
    nums.insert(0, i)
print(nums)  # [2, 1, 0]


print("*********************************************")
# remove(value) – Remove first occurrence of a value
# Example 1
fruits = ['apple', 'banana', 'apple']
fruits.remove('apple')
print(fruits)  # ['banana', 'apple']

# Example 2: Use condition
if "banana" in fruits:
    fruits.remove('banana')

# Example 3: Remove during loop (safe way)
colors = ['red', 'blue', 'red']
for color in colors[:]:  # Copy list to avoid modifying during iteration
    if color == 'red':
        colors.remove(color)
print(colors)


print("****************************************")

# pop(index) – Remove item at index (default is last)
# Example 1
items = ['pen', 'pencil', 'eraser']
removed = items.pop()
print(removed, items)

# Example 2
if len(items) > 0:
    items.pop(0)

# Example 3
stack = [10, 20, 30]
while stack:
    print("Popped:", stack.pop())

# sort() – Sorts list in-place
# Example 1
numbers = [5, 2, 9]
numbers.sort()
print(numbers)

# Example 2: Sort descending
numbers.sort(reverse=True)

# Example 3: Sort strings
names = ['Ali', 'Bilal', 'Ahmed']
names.sort()
print(names)

print("****************************************")

    #   reverse() – Reverses the list in-place

# Example 1
a = [1, 2, 3]
a.reverse()
print(a)

# Example 2: Reverse only if list not empty
if a:
    a.reverse()

# Example 3: Reverse inside loop
nums = [1, 2, 3, 4]
for _ in range(2):
    nums.reverse()
print(nums)

print("***************************************")
# count(value) – Count how many times value appears
# Example 1
votes = ['yes', 'no', 'yes']
print(votes.count('yes'))

# Example 2: Count inside loop
colors = ['red', 'blue', 'red']
for color in set(colors):
    print(color, "count:", colors.count(color))

# Example 3
marks = [50, 70, 70, 90]
if marks.count(70) > 1:
    print("Duplicate marks found")


print("********************************")

# index(value) – Find first index of value
# Example 1
names = ['Ali', 'Sara', 'Ali']
print(names.index('Ali'))  # 0

# Example 2: Check before find
if 'Sara' in names:
    print("Index:", names.index('Sara'))

# Example 3: With try-except
try:
    idx = names.index('Hamza')
except ValueError:
    print("Name not found")


print("****************************************")


# clear() – Empties the entire list
# Example 1
items = ['box', 'bag']
items.clear()
print(items)

# Example 2: Clear if list is not empty
if items:
    items.clear()

# Example 3: Reset list inside loop
records = [1, 2, 3]
for _ in range(1):
    records.clear()
print(records)


print("****************************************")

# copy() – Returns shallow copy (not original reference)
# Example 1
list1 = [10, 20]
list2 = list1.copy()
list2.append(30)
print(list1, list2)

# Example 2: Copy before modifying
original = ['a', 'b']
backup = original.copy()
original.append('c')

# Example 3: Safe copy in function
def modify(data):
    safe = data.copy()
    safe.append("new")
    return safe




print("**********************************************")
# extend(iterable) – Adds each element of iterable to end of list# Example 1
list1 = [1, 2]
list1.extend([3, 4])
print(list1)

# Example 2: Extend with loop data
data = []
for i in range(3):
    data.extend([i])
print(data)

# Example 3: Extend only if input is valid
more = [5, 6]
if isinstance(more, list):
    data.extend(more)
