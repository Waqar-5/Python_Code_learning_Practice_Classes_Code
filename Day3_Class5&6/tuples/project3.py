print("📊 Welcome to Your Monthly Budget Tracker")
print("-" * 50)

# Get monthly income from user
monthly_income = int(input("Enter your monthly income (Rs): "))

# Ask how many expense categories
num_expenses = int(input("How many expense categories do you want to enter? "))

# Build tuple of (category, amount)
expense_list = []
for i in range(num_expenses):
    category = input(f"Enter name of expense #{i+1}: ")
    amount = int(input(f"Enter amount for {category} (Rs): "))
    expense_list.append((category, amount))

# Convert list to tuple of expenses
monthly_expenses = tuple(expense_list)

# Calculate total expense
total_expense = 0
for category, amount in monthly_expenses:
    total_expense += amount

# Show detailed expense report
print("\n📋 Monthly Expense Summary")
print("-" * 50)
for category, amount in monthly_expenses:
    print(f"{category:<20}: Rs {amount}")

print("-" * 50)
print(f"Total Expense       : Rs {total_expense}")
print(f"Monthly Income      : Rs {monthly_income}")

# Final result
print("-" * 50)
if total_expense < monthly_income:
    print(f"✅ Great! You saved Rs {monthly_income - total_expense}")
elif total_expense == monthly_income:
    print("⚠️ No savings. You broke even.")
else:
    print(f"❌ Overspent by Rs {total_expense - monthly_income}")
