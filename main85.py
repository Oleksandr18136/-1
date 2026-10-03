# Get 4-digit number
n = int(input("Введіть чотиризначне число: "))

# Get digits
d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

# Check symmetry (1 = symmetric)
result = (d1 - d4) ** 2 + (d2 - d3) ** 2 + 1

# Print result
print("Результат перевірки симетрії (1 = симетричне):", result)
