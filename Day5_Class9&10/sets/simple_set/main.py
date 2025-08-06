# Creating a Set

# Creating a normal set
my_set = {1,2,3,4}
print("Set: ", my_set)
print(type(my_set))

print("*****************************************")

# .add() – Add a single element

my_set = {1,2,3}
print("Before add: ", my_set)  # {1,2,3,4}
my_set.add(4)
print("After add: ", my_set)  # {1,2,3,4}




print("**********************************")

# .update() – Add multiple elements
print("Before update: ", my_set)

my_set.update([5, 6], {7, 8})
print("After update: ", my_set)  # {1, 2, 3, 4, 5, 6, 7, 8}



print("***********************************")
# .remove() – Remove an element (raises error if not found)
print("Before remove: ", my_set)

my_set.remove(3)
print("After remove: ", my_set) # {1, 2, 4, 5, 6, 7, 8}
# my_set.remove(99)  # ❌ KeyError if element not found


print("***********************************")
# .discard() – Remove element (no error if not found)
print("Before discard: ", my_set)

my_set.discard(2)
my_set.discard(99) # no error
print("After discard: ", my_set) # {1, 4, 5, 6, 7, 8}

print("*******************************")
# .pop() – Remove and return a random element
print("Before pop: ", my_set)

removed = my_set.pop()
print("Popped element:", removed)
print("After pop:", my_set)


print("**********************************")
# .clear() – Remove all elements

print("Before clear: ", my_set)

my_set.clear()
print("After clear:" , my_set) # set()


print("*******************************")
# .copy() – Create a shallow copy

original = {10, 20, 30}
print("Original set ", original)
copy_set = original.copy()
print("Copied set:", copy_set)


print("********************************")
# .union() or | – Combine sets
a = {1, 2}
b = {2, 3, 4}
print("Before union:", "a => ", a, "\nb =>", b)

# union_set = a.union(b) #or
union_set = a | b
print("After Union:", union_set)  # {1, 2, 3, 4}


print("*****************************")
# .intersection() or & – Common elements
print("Before intersection:", "a => ", a, "\nb =>", b)

intersection = a.intersection(b)  # or
# intersection = a & b
print("After Intersection:", intersection)  # {2}

print("************************************")
# .difference() or - – Elements in one set not in another

print("Before Difference:", "a => ", a, "\nb =>", b)

diff = a.difference(b) # or
# diff = a - b
print("After Difference (a - b):", diff)  # {1}

print("****************************************")
# .symmetric_difference() or ^ – Elements in either but not both
print("Before Symmetric Difference:", "a => ", a, "\nb =>", b)

sym_diff = a.symmetric_difference(b) # or
# sym_diff = a^b
print("After Symmetric Difference: ", sym_diff)    # {1, 3, 4}

print("***********************************")

# .issubset() – Checks if all elements of one set are in another


small = {1, 2}
big = {1, 2, 3, 4}

print("Before Is subset:", "small  => ", small , "\nbig  =>", big )

print("After Is subset:", small.issubset(big))  # True

print("**************************")

# .issuperset() – Checks if a set contains another

print("Before Is superset:", "small  => ", small , "\nbig  =>", big )

print("After Is superset:", big.issuperset(small))  # True


print("**************************")

#.isdisjoint() – True if sets have no elements in common
x = {10, 11}
y = {12, 13}

print("Before Is disjoint:", "x  => ", x , "\ny  =>", y )

print("After Is disjoint:", x.isdisjoint(y))  # True
