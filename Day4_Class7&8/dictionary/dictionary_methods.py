# Most Used Dictionary Methods

# Initial dictionary
student = {"name": "Ali", "age": 21, "grade": "A"}

# get(): Safely fetch value by key
print("Original dictionary: ", student)
print("\nAfter get name by using get methods, Name: ", student.get("name")) #output: Ali

print("************************************")



# Convert items to list of tuples
all_items = list(student.items())
print((all_items))
# print(type(all_items)) # <class 'list'>

print("**********************************")
student = {"name": "Ali", "age": 21, "grade": "A"}
print(student.items())
# print(type(student)) #<class 'dict'>
# Output: dict_items([('name', 'Ali'), ('age', 21), ('grade', 'A')])

print("****************************************")
# Access Specific Key-Value Pair by Index
# Get first item
first_key, first_value = list(student.items())[0]
print(f"{first_key} → {first_value}")
# Output: name → Ali

# Get second item
second = list(student.items())[1]
print(f"{second[0]} → {second[1]}")
# Output: age → 21


print("********************************************")
# Unpack All Items One by One (Manually)
(k1, v1), (k2, v2), (k3, v3) = student.items()

print(f"{k1} → {v1}")
print(f"{k2} → {v2}")
print(f"{k3} → {v3}")


print("****************************************")
# keys(): Get all keys
print("original dictionary: ", student)
print("Keys:", list(student.keys()))  # ['name', 'age', 'grade']

print("*************************************")
print("original dictionary: ", student)
# values(): Get all values
print("Values: ", list(student.values())) # ['Ali', 21, 'A']

print("********************************************")

# update(): Add or update keys from another dictionary
print("original dictionary: ", student)
student.update({"age": 22, "subject": "Math"})
print("Updated: ", student) # 'age' updated, 'subject' added


print("********************************************")
# pop(): Remove specific key
print("original dictionary: ", student)
age = student.pop("age")
print("Removed Age:", age)
print("After pop:", student)



print("**************************************")
# clear(): Remove all key-value pairs
print("original dictionary: ", student)
backup = student.copy()  # Before clearing
student.clear()
print("After clear: ", student) #{}


print("*************************************")
print("original dictionary: ", student)

# copy(): Create a shallow copy of dict
new_student = backup.copy()
print("Copied Dict: ", new_student)
# print(type(new_student))




print("******************************************************")
print("less used methods.............")
# Less Used Methods
# setdefault(): If key not found, set it with default value
print("original dict: ", new_student)

new_student.setdefault("city", "Lahore")  # city is added
print("After setdefault: ", new_student)

print("**************************************")
print("original dict: ", new_student)
# fromkeys(): Create new dict from keys with same default value
subjects = ["Math", "English", "Science"]
default_marks = dict.fromkeys(subjects, 0)
print("after using Fromkeys:", default_marks)  # {'Math': 0, 'English': 0, 'Science': 0}

print("*********************************")
print("original dict: ", new_student)
# popitem(): Removes the last inserted key-value pair
last = new_student.popitem()
print("Removed last item:", last)
print("After popitem:", new_student)


print("************************************************")
print(" Rarely Used or Internal Dunder Methods")
# Rarely Used or Internal Dunder Methods
# __contains__(): Check if key exists (like `in`)
print("original dict: ", new_student)
print("Has 'name'?", new_student.__contains__("name"))  # True

print("**************************************")
print("original dict: ", new_student)
# __len__(): Length of dictionary (like len(dict))
print("Length:", new_student.__len__())  # Same as len(new_student)

print("*************************************")
print("original dict: ", new_student)
# __delitem__(): Delete a key manually
new_student.__delitem__("name")
print("After __delitem__:", new_student)

print("****************************************")
print("original dict: ", new_student)
# __setitem__(): Set or update key manually
new_student.__setitem__("name", "Ahsan")
print("After __setitem__:", new_student)


print("********************************************")
print("original dict: ", new_student)
# __getitem__(): Get a value by key manually
print("Using __getitem__:", new_student.__getitem__("name"))
