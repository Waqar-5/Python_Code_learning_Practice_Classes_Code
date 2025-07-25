# Immutable Monthly Budget Tracker
# Tuple of (category, amount)
monthly_expenses = (
    ("Rent", 25000),
    ("Food", 10000),
    ("Utilities", 5000),
    ("Transport", 3000),
    ("Entertainment", 2000),
)

monthly_income = 50000

# Calculate total expenses
total_expense = 0
for item in monthly_expenses:
    category, amount = item
    total_expense += amount

# Display summary
print("Monthly Expense Summary")
print("-" * 30)
for category, amount in monthly_expenses:
    print(f"{category:<15}: Rs {amount}")

print("\nTotal Expense     :", total_expense)
print("Monthly Income    :", monthly_income)

# Condition to check financial status
if total_expense < monthly_income:
    print("✅ You saved:", monthly_income - total_expense)
elif total_expense == monthly_income:
    print("⚠️ No savings, no loss!")
else:
    print("❌ Over budget by:", total_expense - monthly_income)
