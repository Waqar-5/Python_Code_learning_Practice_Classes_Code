# 🧠 Student Progress Tracker using only list, loops, conditions, and operators

# Initial empty lists
students = []
scores = []

# 1️⃣ Add Students
print("Enter student names (type 'done' to stop):")
while True:
    name = input("Name: ")
    if name.lower() == 'done':
        break
    if name not in students:
        students.append(name)
    else:
        print("Duplicate name! Skipped.")

# 2️⃣ Add Scores (parallel list)
print("\nNow enter scores out of 100 for each student:")
for student in students:
    while True:
        try:
            score = int(input(f"{student}'s score: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Score must be between 0 and 100.")
        except:
            print("Enter valid integer.")

# 3️⃣ Display Results
print("\n🎯 All Students and Scores:")
for i in range(len(students)):
    print(f"{students[i]} - {scores[i]}")

# 4️⃣ Show Toppers (score > 90)
print("\n🏆 Toppers (score > 90):")
for i in range(len(scores)):
    if scores[i] > 90:
        print(f"{students[i]} - {scores[i]}")

# 5️⃣ Remove absent students (score == 0)
print("\n❌ Removing absent students (0 score)...")
i = 0
while i < len(scores):
    if scores[i] == 0:
        print(f"Removed: {students[i]}")
        students.pop(i)
        scores.pop(i)
    else:
        i += 1

# 6️⃣ Insert Bonus Points for specific student
bonus_student = input("\nEnter student name to give 5 bonus points: ")
if bonus_student in students:
    index = students.index(bonus_student)
    scores[index] += 5
    print(f"🎁 Bonus added to {bonus_student}!")
else:
    print("Student not found.")

# 7️⃣ Sort Students by Score
print("\n📊 Sorting students by scores (descending)...")
sorted_students = students.copy()
sorted_scores = scores.copy()

# Bubble sort (manual logic)
for i in range(len(sorted_scores)):
    for j in range(i + 1, len(sorted_scores)):
        if sorted_scores[i] < sorted_scores[j]:
            # Swap scores
            sorted_scores[i], sorted_scores[j] = sorted_scores[j], sorted_scores[i]
            # Swap names in same order
            sorted_students[i], sorted_students[j] = sorted_students[j], sorted_students[i]

for i in range(len(sorted_students)):
    print(f"{sorted_students[i]} - {sorted_scores[i]}")

# 8️⃣ Count how many got 100
perfect_scores = scores.count(100)
print(f"\n✅ Number of students who scored 100: {perfect_scores}")

# 9️⃣ Reverse list (for fun)
print("\n🔁 Students in reverse order:")
students.reverse()
for name in students:
    print(name)

# 🔟 Clear Everything (End of session)
clear_data = input("\nClear all data? (yes/no): ")
if clear_data.lower() == 'yes':
    students.clear()
    scores.clear()
    print("🧹 Data cleared.")
else:
    print("📁 Data retained.")
