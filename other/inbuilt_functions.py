#!/bin/python3

import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"
grades = [int(x) for x in data.split(',')]
print(f"Grades: {grades}")

# 4. Display the minimum value of the grades.
grades.sort()
print(f"Minimum value: {grades[0]}")

# 5. Display the maximum value of grades.
print(f"Maximum value: {grades[-1]}")

# 9. Display the average of grades to two decimal points.
# Tip: use the sum(), len() and round() functions.
my_mean = round(sum(grades) / len(grades), 2)
print(f"Mean grade using my own maths: {my_mean}")

# 11. Use the statistics' mean() function to get the average grade to two decimal places.
statistics_mean = round(statistics.mean(grades), 2)
print(f"Mean grade using the statistics library: {statistics_mean}")

# 12. Display the median values using the statistics.median() function.
# The median is the value that appears in the middle of your dataset, after
# you’ve arranged the data in value order (i.e. lowest to highest, or highest to
# lowest).
statistics_median = round(statistics.median(grades))
print(f"Median grade using the statistics library: {statistics_median}")
