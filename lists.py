#!/bin/python3

ages = [12, 18, 33, 84, 45, 67, 12, 82, 95, 16, 10, 23, 43, 29, 40, 34, 30, 16, 44, 69, 70, 74, 38, 65, 36, 83, 50, 11, 7, 9, 64, 78, 37, 3, 8, 68, 22, 4, 60, 33, 82, 45, 23, 5, 18, 28, 99, 17, 81, 14, 88, 50, 19, 59, 7, 44, 93, 35, 72, 25, 63, 11, 69, 11, 76, 10, 60, 30, 14, 21, 82, 47, 6, 21, 88, 46, 78, 92, 48, 36, 28, 51]

# Print the length of the list
length_of_ages = len(ages)
print(length_of_ages)

# Print each age in the list
for age in ages:
    print(age)

# Add one to each age in the list
for i in range(0, len(ages), 1):
    ages[i] += 1

# Print each age in the list
for age in ages:
    print(age)

# Count how many ages are between 16 and 25 (inclusive)
count = 0
for age in ages:
    if 16 <= age <= 25:
        count += 1

# Print the number of ages between 16 and 25 (inclusive)
print(f"Total number of ages between 16 and 25 is {count}")

# Sort the ages in ascending order
ages.sort()

# Print each age in the list
for age in ages:
    print(age)

# Find the proportion of ages between 16 and 25
proportion = round(len(ages) / count, 1)
print(f"Proportion of ages between 16 and 25 is {proportion}%")
