# Get total seconds
total_seconds = int(input("Введіть кількість секунд: "))

# Calculate days, hours, minutes, seconds
days = total_seconds // 86400
remaining = total_seconds % 86400

hours = remaining // 3600
remaining = remaining % 3600

minutes = remaining // 60
seconds = remaining % 60

# Print result
print("Перетворений час:", days, "днів,", hours, "годин,", minutes, "хвилин,", seconds, "секунд.")