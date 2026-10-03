import math

# Get side lengths
a = float(input("Введіть сторону a: "))
b = float(input("Введіть сторону b: "))
c = float(input("Введіть сторону c: "))

# Calculate semi-perimeter
p = (a + b + c) / 2

# Calculate area
area = math.sqrt(p * (p - a) * (p - b) * (p - c))

# Print result
print("Площа трикутника:", area)