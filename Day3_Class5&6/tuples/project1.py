# Project 1: Student Gradebook (Immutable Record System)
# Tuple of student records: (name, marks)
students = (
    ("Ali", 85),
    ("Sara", 92),
    ("Ahmed", 76),
    ("Zara", 59),
    ("Bilal", 67),
)

# Function to assign grades
def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Process each student
print("Student Report Card:")
print("-" * 30)
for student in students:
    name, marks = student
    grade = assign_grade(marks)
    print(f"Name: {name}, Marks: {marks}, Grade: {grade}")
