"""
📝 Assignment Statement
Title:
🎓 Student Grading and Class Topper Finder using Dictionaries and Lists in Python

Objective:
To design a Python program that collects student marks for multiple classes, categorizes the students into grade levels (A+, A, B), and identifies the top scorer in each class. The program uses core data structures such as dictionaries, lists, and tuples, along with loops and conditionals.

Task Description:

Create a dictionary that stores student data (name and marks) for each class.

Take input from the user to add student names and their marks for Class 1, Class 2, and Class 3.

Validate the entered marks to ensure they are between 0 and 100.

Classify students into the following grade categories based on their marks:

A+ ➤ 90–100

A ➤ 70–89

B ➤ 60–69

Identify and display the highest scoring student (topper) from each class.

Display all students in each grade category, along with their class name and marks.

Tools and Concepts Used:

Python dictionary to group classes.

List of tuples to store (name, marks).

input() for dynamic data entry.

Conditional logic (if, elif) for grading.

max() function with lambda for finding class toppers.

Loops (for, while) for data entry and processing.

or 
Assignment Statement (Simple)
Take marks of students from each class.

Store names and marks in a list.

Check scores and put in grade lists:

A+ for 90 to 100

A for 70 to 89

B for 60 to 69

Show which student got highest marks in each class.

Use dictionary, lists, loops, and conditions.
"""


# 📘 Step 1: Create a dictionary to store (name, marks) tuples of students in each class
classes = {
    "Class 1": [],
    "Class 2": [],
    "Class 3": []
}

# 📥 Step 2: Input student names and marks for each class
for class_name in classes:
    print(f"\n🔹 Enter name and marks for students in {class_name} (type 'done' to stop):")
    
    while True:
        name = input("👤 Enter student name: ")
        if name.lower() == 'done':
            break

        mark = input(f"➤ Enter marks for {name}: ")
        
        if mark.isdigit():
            mark_int = int(mark)
            if 0 <= mark_int <= 100:
                classes[class_name].append((name, mark_int))
            else:
                print("⚠️ Marks must be between 0 and 100.")
        else:
            print("❌ Invalid marks! Only numbers allowed.")

# 🏷️ Step 3: Create grade lists for categorization
grade_A_plus = []  # ➕ 90-100
grade_A = []       # ✅ 70-89
grade_B = []       # 📘 60-69

# 🧮 Step 4: Categorize students into grade lists
for class_name, students in classes.items():
    for name, mark in students:
        if mark >= 90:
            grade_A_plus.append((class_name, name, mark))  # 🎓 A+
        elif mark >= 70:
            grade_A.append((class_name, name, mark))       # ✅ A
        elif mark >= 60:
            grade_B.append((class_name, name, mark))       # 📘 B

# 🏆 Step 5: Find highest scorer in each class
print("\n🎓 Topper in Each Class:")
for class_name, students in classes.items():
    if students:
        topper = max(students, key=lambda x: x[1])  # sort by marks
        print(f"{class_name} ➤ 🥇 {topper[0]} scored: {topper[1]} marks")
    else:
        print(f"{class_name} ➤ No data entered ❌")

# 📊 Step 6: Show all grade lists
print("\n🏅 Grade A+ (90-100):")
for class_name, name, mark in grade_A_plus:
    print(f"{class_name} ➤ {name} ➤ {mark} marks")

print("\n✅ Grade A (70-89):")
for class_name, name, mark in grade_A:
    print(f"{class_name} ➤ {name} ➤ {mark} marks")

print("\n📘 Grade B (60-69):")
for class_name, name, mark in grade_B:
    print(f"{class_name} ➤ {name} ➤ {mark} marks")
