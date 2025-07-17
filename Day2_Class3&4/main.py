# Concatenation
"""
String Output Methods
➤ Comma Strings (Auto space)
"""

print("using comma strings: ")
name = "Waqar Ali"
a = 25
status = True
pi = 3.14

print("Name: ", name, "Age: ", a)
print("Active: ", status)
print("Pi vaue is: ", pi)
print("ID: ", 123, "User:", name)
print("Python", "is", "fun!")

print("**********************************")

print("F-Strings: ")
print(f"My name is {name}")
print(f"{name} is {a} years old")
print(f"pi = {pi}")
print(f"Status: {'Active' if status else 'Inactive'}")
print(f"{name.upper()} is a great programmer")


print("**********************************")
print(".format() Method: ")
print("Hello, {}, Age: {}".format(name, a))
print("Pi is {:.2f}".format(pi))
print("{} is learning {}".format(name, "Pakistan"))
print("Status: {}".format("Active" if status else "Offline"))
print("Your ID is: {}".format(123))

print("**********************************")
print("Conversion from String to Int (Valid)")

print(int("10"))  #10
print(int("007")) #7
print(int("0")) #0
print(int("1000")) #1000
print(int("42")) #42
print(int("123456789")) #123456789

# 🛑 Note: int("abc") will give ValueError



print("**********************************")


# Conditions

age = 18
if age >= 18:
    print("You can vote!")


print("**********************************")
score = 45
if score > 50:
    print("Fail")
else:
    print("Pass")

print("**********************************")
x = 70
if x > 90:
    print("Grade A+")
elif x > 80:
    print("Grade A")
else:
    print("Grade B")

print("**********************************")
if name == "Ali":
    print("Welcome Ali!")

if not status:
    print("Offline")
else:
    print("Online")


print("**********************************")
# Methods like .lower(), .upper(), .replace()
print("Hello".lower()) # hello
print("Hello".upper()) # HELLO
print("     Hello    ".strip()) # spacedHello
print("python".capitalize()) #Python
print("data science".replace(" ", "-")) #data-science   


print("**********************************")
# Nested Conditions

age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Entry allowed")


x = 90
if x > 50:
    if x > 80:
        print("Excellent")

print("**********************************")

admine = "admin"
if admine == "admin":
    if status:
        print("Access granted")

if name == "Ahmed":
    if len(name) == 5:
        print("Short name")
a1 = 9
if a1 > 0:
    if a1 % 3 == 0:
        print("a is divisible by 3")



print("**********************************")

# for loop (controlled)
for i in range(5):
    print(i)

print("**********************************")

for letter in "Hi":
    print(letter)

print("**********************************")

for num in [2, 4, 6]:
    print(num)

print("**********************************")

for i in range(0, 10, 2):
    print(f"step: {i}")

print("**********************************")

names = ["Ali", "Sara", "Khan"]
for n in names:
    print(f"Hello {n}")



#  while loop (uncontrolled)
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

print("**********************************")

password = ""
while password != "1234":
    password = "1234" # Simulating correct input
    print("Verifying password...")

print("***********************************")

x = 3
while x > 0:
    print(x)
    x -= 1

print("**********************************")

tries = 0
while True:
    print("Attempt:", tries)
    tries += 1
    if tries == 3:
        break
print("**********************************")


choice = ""
while choice != "exit":
    choice = "exit"
    print("Menu loop running...")