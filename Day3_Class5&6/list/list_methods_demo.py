# Start with a basic list of students
students = ["Ali", "Fatima", "Usman", "Zara"]
print("Original list: ", students)

# Add a new student at the end
students.append("Aliza")
print("after adding element in end: ", students)

# Insert a student at the index 3
students.insert(2, "bilal")
print("after inserting at index 2 name bilal: ", students)

# remove a student by name
students.remove("Fatima")
print("after remove a student through name: ", students)

# Sort the list alphabetically
students.sort()
print("after sorting list: ", students)


# reverse the order
students.reverse()
print("After reversing list: ", students)


# count how many times a name appears
count = students.count("Usman")

# Display the final list
print("Updated Students List:", students)
print("Usman appears:", count, "time(s)")