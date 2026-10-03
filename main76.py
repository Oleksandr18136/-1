# Get days
days = int(input("Введіть кількість днів: "))

# Calculate time units
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

# Print formatted result
print("Тривалість канікул:")
print(f"{hours:<10}годин")
print(f"{minutes:<10}хвилин")
print(f"{seconds:<10}секунд")