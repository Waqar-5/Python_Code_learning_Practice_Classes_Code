
name = "Meer Ali"
age = 20
grade = "A"
is_enrolled = True
score = 70

print(name)  # Meer Ali
print(age)   # 20
print(grade)  # A
print(is_enrolled)  # True
print(score)  # 70

print(f"{name} is {age} years old with grade {grade} and score {score}.")



print("**********************************")

a = 20
b = 10
print("a =", a)  # 20
print("b =", b)  # 10
print("Sum of a and b is  = ",a + b)  # 30
print("Subtraction of a and b is = ",a - b)  # 10
print("Multiplication of a and b is  = ",a * b)  # 200
print("Division of a and b is = ",a / b)  # 2.0
print("Floor Division:", a // b)  # 2
print("Remainder:", a % b)        # 0


# Assignment 3: Swap Variables
x = 5
y = 10
print("Before swapping: x =", x, ", y =", y)  # x = 5, y = 10
x, y = y, x  # Swapping values
print("After swapping: x =", x, ", y =", y)  # x = 10, y = 5
