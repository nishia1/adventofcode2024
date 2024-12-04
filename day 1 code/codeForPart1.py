import math

# Read the file
with open("day 1 code/dayOneInput.txt", 'r', encoding='utf-8') as file:
    content = file.read().splitlines()
#with open("day 1 code/randomTestingNumbers.txt", 'r', encoding='utf-8') as file:
#    content = file.read().splitlines()
l1 = []
l2 = []

# Process each line in the file
for line in content:
    parts = line.split()  # Automatically split by any whitespace
    l1.append(int(parts[0]))  # Convert and append the first number
    l2.append(int(parts[1]))  # Convert and append the second number
l2.sort()
l1.sort()
total_sum = 0

# Calculate the sum of absolute differences
for i in range(len(l1)):
    total_sum += abs(l1[i] - l2[i])

print(total_sum)