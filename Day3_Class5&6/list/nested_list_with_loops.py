products = [
    ["Apple", 120],
    ["Banana", 50],
    ["Mango", 100],
    # ["Mango", 100],
    # ["Mango", 100]
]
print("🔍 Product List (using nested loop):")
for product in products:
    for item in product:
        print("1",item)

print("*****************************************")

products = [
    ["Apple", 120],
    ["Banana", 50],
    ["Mango", 100],
    # ["Mango", 100],
    # ["Mango", 100]
]
for i, product in enumerate(products):
    print(f"\n📦 Product {i + 1}")
    for j, value in enumerate(product):
        print(f"  - Element {j + 1}: {value}")

print("*********************************************")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("🧮 Matrix View:")
for row in matrix:
    for col in row:
        print(col, end=" ")
    print() # new line after each row

print("**************************************")
# Get only second item from each inner list
print("💲 Only prices:")
for product in products:
    # print(product[0])
    print(product[1])

print("***********************************")
# With condition – show products > 60
print("💡 Products with price > 60:")
for name, price in products:
    if price > 60:
        print(name, "=>", price)

print("****************************************")
products = [
    ["Apple", 120],
    ["Banana", 50],
    ["Mango", 100, ["Mango", 100, ["Mang", 0]]], 
]
def print_items(data):
    for item in data:
        if isinstance(item, list):  # if item is a list, go deeper
            print_items(item)
        else:
            print(item)

# Call the function
print("🔍 Product List (recursive deep loop):")
print_items(products)

print("*********************************************")
products = [
    ["Apple", 120],
    ["Banana", 50],
    ["Mango", 100, ["Mango", 100, ["Mang", 0]]],
]

print("🔁 Product List (loop-only deep traversal):")

stack = [products]  # start with outer list

while stack:
    current = stack.pop(0)  # get first item from stack
    for item in current:
        if isinstance(item, list):
            stack.insert(0, item)  # add nested list at beginning to process it next
        else:
            print(item)

print("**********************************")
# # Step-by-step loop-based navigation
# level1 = products[2][2][2]              # ["Mango", 100, ["Mango", 100, ["Mang", 0]]]
# # level2 = level1[2]                # ["Mango", 100, ["Mang", 0]]
# # level3 = level2[2]                # ["Mang", 0]

# print("📦 Final deeply nested list:", level1)

# current = products
# for i in [2, 2, 2]:  # indexes to go deeper
#     current = current[i]

# print("🔍 Reached:", current)  # ['Mang', 0]

print("*************************************************")

p1 = [["Ali", "Khan"], ["sohail", "sami", ["someone","me"]]]
for i in p1:
    for item in i:
        if type(item) == list:
            for i in item:
                print(i)
        else:
            print(item)



print("****************************************")
p1 = [["Ali", "Khan"], ["sohail", "sami", ["someone", "me", [1, 2, 3, ["Khan"]]]]]

for i in p1:
    for item in i:
        if type(item) == list:
            for i in item:
                print(i)
        else:
            print(item)


print("*********************************************")
#  If You Want Deep Levels (Recursive):
# You need recursive function:
def print_items(data):
    for item in data:
        if isinstance(item, list):
            print_items(item)
        else:
            print(item)

p1 = [["Ali", "Khan"], ["sohail", "sami", ["someone", "me", [1, 2, 3, ["Khan"]]]]]
print_items(p1)

print("**************************************************")
p1 = [
    ["Ali", "Khan"],
    ["sohail", "sami", [
        "someone", "me", 
        [1, 2, 3, 
            ["Khan", 
                ["meer", 
                    ["Khan"]
                ]
            ]
        ]
    ]]
]

print("📜 All Items in List:")
stack = p1.copy()  # Make a copy to avoid changing original
while stack:
    item = stack.pop(0)  # Get the first item
    if isinstance(item, list):
        stack = item + stack  # Flatten the current list into front
    else:
        print(item)

print("**************************************")
def print_items(data):
    for item in data:
        if isinstance(item, list):
            print_items(item)  # 🔁 Go deeper if item is a list
        else:
            print(item)       # ✅ Print when item is not a list

# Your deeply nested list
p1 = [
    ["Ali", "Khan"], 
    ["sohail", "sami", [
        "someone", "me", 
        [1, 2, 3, 
            ["Khan", 
                ["meer", 
                    ["Khan", ["meer"], ["meer"]]
                ]
            ]
        ]
    ]]
]

# Run the recursive function
print("📜 All Items (Recursive):")
print_items(p1)



p1 = [
    ["Ali", "Khan"], 
    ["sohail", "sami", [
        "someone", "me", 
        [1, 2, 3, 
            ["Khan", 
                ["meer", 
                    ["Khan"]
                ]
            ]
        ]
    ]]
]

for a in p1:
    if isinstance(a, list):
        for b in a:
            if isinstance(b, list):
                for c in b:
                    if isinstance(c, list):
                        for d in c:
                            if isinstance(d, list):
                                for e in d:
                                    if isinstance(e, list):
                                        for f in e:
                                            print(f)
                                    else:
                                        print(e)
                            else:
                                print(d)
                    else:
                        print(c)
            else:
                print(b)
    else:
        print(a)
print("*****************************************")
p1 = [
    ["Ali", "Khan"], 
    ["sohail", "sami", [
        "someone", "me", 
        [1, 2, 3, 
            ["Khan", 
                ["meer", 
                    ["Khan"]
                ]
            ]
        ]
    ]]
]

def print_items_stack(data):
    stack = [data]  # start with the outermost list

    while stack:
        current = stack.pop()
        if isinstance(current, list):
            # Add all elements in reverse order so they come out in correct order
            stack.extend(reversed(current))
        else:
            print(current)

print("📜 All Items (Using Stack):")
print_items_stack(p1)
