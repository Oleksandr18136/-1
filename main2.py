# Get number as string
n_str = input("Введіть число n: ")

# Convert to integers: n, nn, nnn
n1 = int(n_str)
n2 = int(n_str * 2)
n3 = int(n_str * 3)

# Calculate sum
result = n1 + n2 + n3

# Print result
print("Результат виразу n + nn + nnn:", result)