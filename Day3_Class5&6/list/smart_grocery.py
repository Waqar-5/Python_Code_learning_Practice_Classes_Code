# Smart Grocery Bag 🛒
# Author: Waqar Ali
# GitHub: https://github.com/yourrepo/smart-grocery-bag

print("🛒 Welcome to Smart Grocery Bag 🛒")
print("Type 'exit' to finish!\n")

grocery_list = []
unhealthy_items = ["soda", "chips", "candy", "burger", "fry", "fries"]

while True:
    item = input("Add grocery item: ").lower()
    
    if item == "exit":
        break

    # Add only if not duplicate
    if item not in grocery_list:
        grocery_list.append(item)
        print(f"✅ '{item}' added to the grocery bag.")
        
        # Warning for unhealthy items
        if item in unhealthy_items:
            print(f"⚠️ Warning: '{item}' is considered unhealthy!")
    else:
        print(f"🔁 '{item}' is already in the grocery bag.")

print("\n🧾 Final Grocery List:")
for index, item in enumerate(grocery_list, 1):
    print(f"{index}. {item}")

# Count total items
print(f"\n📦 Total Items: {len(grocery_list)}")

# Filter by condition: Show only fruits (simulate with known names)
fruits = ["apple", "banana", "mango", "grape", "orange", "kiwi"]
fruit_only = []

for item in grocery_list:
    if item in fruits:
        fruit_only.append(item)

if fruit_only:
    print("\n🍎 Fruits in your bag:")
    for fruit in fruit_only:
        print(f"✔️ {fruit}")
else:
    print("\n🚫 No fruits in your grocery list.")

# Remove item feature (simulate conditions)
remove_item = input("\nDo you want to remove any item? Type name or 'no': ").lower()
if remove_item in grocery_list:
    grocery_list.remove(remove_item)
    print(f"❌ '{remove_item}' removed.")
elif remove_item != "no":
    print(f"❌ '{remove_item}' not found in your list.")

# Final result after removal
print("\n📦 Updated Grocery Bag:")
for i, item in enumerate(grocery_list, 1):
    print(f"{i}. {item}")
