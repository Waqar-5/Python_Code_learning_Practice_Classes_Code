# Creating a frozenset
a = frozenset([1, 2, 3])
b = frozenset([3, 4, 5])
print("Set A:", a)
print("Set B:", b)

print("***************************")
# All Set Operations Supported on frozenset
# 🎯 1. .union() or |
print("Before union in frozenset: ", "a =>", a, "\nb =>", b)

result = a.union(b) # or
# result = a|b
print("After frozenset Union:", result)  # frozenset({1, 2, 3, 4, 5})


print("***************************")
#  2. .intersection() or &
print("Before Intersection in frozenset: ", "a =>", a, "\nb =>", b)

result = a.intersection(b) # or
# result = a&b
print("After frozenset intersection:", result)    # frozenset({3})




print("***************************")
#  3. .difference() or -
print("Before Difference (a - b) in frozenset: ", "a =>", a, "\nb =>", b)

result = a.difference(b) # or
result = (a - b)
print("After frozenset Difference (a - b)", result)    # frozenset({1, 2})



print("***************************")

#  .symmetric_difference() or ^

print("Before Symmetric Difference: in frozenset: ", "a =>", a, "\nb =>", b)

result = a.symmetric_difference(b) # or
result = (a ^ b)
print("After frozenset Symmetric Difference:", result)    # frozenset({1, 2})





print("***************************")
small = frozenset([1, 2])
#  5. .issubset()

print("Before Is subset:: in frozenset: ", "a =>", a, "\nsmall =>", small)

result = small.issubset(a) # or
print("After frozenset Is subset::", result)  # True   # frozenset({1, 2})

print("***************************")
print("Before  Is superset: in frozenset: ", "a =>", a, "\nsmall =>", small)

print("After frozenset Is superset:", result)  # True   # frozenset({1, 2})

print("***********************************************")

x = frozenset([10, 11])
y = frozenset([12, 13])

print("Before Is disjoint:", "x =>", x, "\ny =>", y )


print("After Is disjoint:", x.isdisjoint(y))  # True


print("****************************************")
# 🧊 Real Use of frozenset
# ✅ Use as a Dictionary Key

my_dict = {frozenset([1, 2]): "valid key"}
print(my_dict)  # {frozenset({1, 2}): 'valid key'}


print("****************************************")

# ✅ Use as a Set Element
nested = {frozenset([10, 20]), frozenset([30, 40])}
print(nested)  # {frozenset({10, 20}), frozenset({30, 40})}





"""
Noticeable
🚫 Methods Not Available in frozenset
❌ Not Allowed =>	Because frozenset is Immutable
.add()	 =>❌ Raises AttributeError
.remove() =>	 ❌ Not supported
.discard() =>	❌ Not supported
.pop() =>	❌ Not supported
.clear() =>	❌ Not supported
.update() =>	❌ Not supported



📝 frozenset Summary Table (Interview-Ready)
Feature	frozenset
Immutable?	           =>    ✅ Yes
Hashable?              => 	 ✅ Yes
Can be a dict key?     =>	 ✅ Yes
Can perform set ops?   =>	 ✅ All except modifying
Methods available      =>	 union, intersection, difference, etc.
Methods not available  =>	 add, remove, discard, pop, update, clear



"""
