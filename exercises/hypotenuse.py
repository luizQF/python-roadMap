import math
a = input("Enter the length of the first side of the triangle: ")
b = input("Enter the length of the second side of the triangle: ")
# Convert the input values to float for calculation
a = float(a)
b = float(b)
c = math.hypot(a, b)
print(f"The length of the hypotenuse is: {c}")