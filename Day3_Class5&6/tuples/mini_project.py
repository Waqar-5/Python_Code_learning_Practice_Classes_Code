students = ("Ali", "Sara", "John", "Lara")
marks = (88, 92, 76, 64)

for i in range(len(students)):
    status = "Pass" if marks[i] >= 70 else "Fail"
    print(f"{students[i]} => Marks: {marks[i]} => {status}")
