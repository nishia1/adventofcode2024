# part 2
# idea is to
# a) get the list from bf
# b) make a dict of number and occurences for both of left and right (num*number)
# c) abs the difference and sum it up

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
l1 = list(set(l1))
total_similiarity_score = 0
# now that i have the lists, create dict with number of occurences for each unique number
for x in l1:
    total_similiarity_score+=((l2.count(x))*x)
print(total_similiarity_score)