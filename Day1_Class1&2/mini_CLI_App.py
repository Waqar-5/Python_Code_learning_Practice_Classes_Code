# 🔥 Build a Mini CLI App:


# Step 1: Take user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_score = int(input("Enter your score: "))

# Step 2: Apply bonus or penalty
adjusted_score = user_score  # Start with original score


if user_age < 18:
    print(f"🎁 Bonus! {user_name}, you are under 18. +5 points added.")
    adjusted_score += 5

elif user_score % 2 == 0:
    print(f"⚠️ Penalty! Your score is even. 2 points subtracted.")
    adjusted_score -= 2

else:
    print(f"✅ No bonus or penalty applied. Your score is odd.")




# Step 3: Show final results
print("📊 Final Result:")
print(f"👤 Name     : {user_name.title()}")
print(f"📅 Age      : {user_age}")
print(f"🎯 Final Score : {adjusted_score}")