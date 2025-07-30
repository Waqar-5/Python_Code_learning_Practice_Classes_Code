# A nested list is a list inside another list


# A simple flat list
simple_list = [10, 20, 30]

# A nested list: each element is itself a list
nested_list = [[10, 20], [30, 40], [50, 60]]

# Extend the first inner list (index -3) with two new elements
# nested_list[-3] == nested_list[0] == [10, 20]
print("Original list: ", nested_list)
nested_list[-3].extend([70, 80])  
print("List after extend it: ",nested_list)  # Output: [[10, 20, 70, 80], [30, 40], [50, 60]]

# Extend the second inner list (index -2) with two new elements
print("Original list: ", nested_list)
# nested_list[-2] == nested_list[1] == [30, 40]
nested_list[-2].extend([70, 80])  
print("List after extend it:",nested_list)  # Output: [[10, 20, 70, 80], [30, 40, 70, 80], [50, 60]]

print("***************************************************")

# Access and Update
# Access the first element of the second inner list
print("Original list: ", nested_list)
print(nested_list[1][0])  # Output: 30


# Change 40 to 45
nested_list[1][1] = 45
print(nested_list)  # Output: [[10, 20], [30, 45], [50, 60, 70, 80]]

print("************************************************")
product_lists = [
    ["Apples", "Bananas"],           # List for Store A
    ["Milk", "Bread", "Eggs"],       # List for Store B
    ["Soap", "Shampoo"]              # List for Store C
]

print("Before Append:", product_lists)
product_lists[0].append("Oranges")
print("After Append to Store A:", product_lists)


print("**************************************************************")
print("Before Extend:", product_lists)
product_lists[1].extend(["Butter", "Cheese"])
print("After Extend Store B:", product_lists)

print("**************************************************************")
print("Before Insert:", product_lists)
product_lists[2].insert(1, "Toothpaste")
print("After Insert in Store C:", product_lists)

print("**************************************************************")

print("Before Remove:", product_lists)
product_lists[1].remove("Milk")
print("After Remove 'Milk' from Store B:", product_lists)

print("**************************************************************")
print("Before Pop:", product_lists)
popped_item = product_lists[2].pop()
print("Popped Item:", popped_item)
print("After Pop from Store C:", product_lists)


print("**************************************************************")
product_lists[0][1] = "Mangoes"
print("After Changing Bananas → Mangoes:", product_lists)

print("Before Update:", product_lists)
print("Before Sort:", product_lists)
product_lists[1].sort()
print("After Sorting Store B:", product_lists)

print("**************************************************************")
print("Before Reverse:", product_lists)
product_lists[0].reverse()
print("After Reversing Store A:", product_lists)

print("**************************************************************")
print("Before Clear:", product_lists)
product_lists[2].clear()
print("After Clearing Store C:", product_lists)

print("**************************************************************")

"""
nested = [[1, 2], [3, 4], [5, 6]]
Now:

nested[0] → [1, 2] (first inner list)

nested[0][0] → 1 (first element of first inner list)

nested[1][1] → 4 (second element of second inner list)

"""

deep = [[[10, 20]], [[30, 40]], [[50, 60]]]
print(deep[0][0][1])  # → 20
