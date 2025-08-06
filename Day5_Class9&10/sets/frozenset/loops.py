# ❄️ Looping Through frozenset in Python
# Just like set, a frozenset is also iterable, so you can loop through its elements using a for loop.


# Basic for Loop on a frozenset
frozen = frozenset([100, 200, 300])

for item in frozen:
    print(f"Item:", item)

print("**********************************")
frozen = frozenset([200, 100, 300])  # Insertion order here matters only at creation

# Convert to list to keep the order
ordered_items = list(frozen)

for i in range(len(ordered_items)):
    print(f"Item{i+1}: {ordered_items[i]}")

print("******************************************")
# Output order is not guaranteed since frozenset is unordered, like set.
# Print Messages for Names
names = frozenset(["Alice", "Bob", "Charlie"])

for name in names:
    print(f"Welcome, {name}!")

print("******************************")

#  Print Squares of Numbers
nums = frozenset([2, 4, 6])

for n in nums:
    print(f"{n} squared is {n ** 2}")

print("*******************************************")
# Filtering During Loop (store in new set)
original = frozenset([5, 10, 15, 20])
greater_than_10 = set()  # Normal set to collect results

for num in original:
    if num > 10:
        greater_than_10.add(num)

print("Filtered set:", greater_than_10)  # {15, 20}
#  Note: You can't use .add() or .remove() on frozenset, so we create a regular set for results.

print("***********************************************")
#  Nested Loop with frozenset
colors = frozenset(["red", "blue"])
shapes = frozenset(["circle", "square"])

for color in colors:
    for shape in shapes:
        print(f"{color} {shape}")

print("*******************************************")
# Convert frozenset to List Inside Loop
fs = frozenset(["Python", "JavaScript", "Go"])

langs = list(fs)

for i in range(len(langs)):
    print(f"Language {i + 1}:", langs[i])
