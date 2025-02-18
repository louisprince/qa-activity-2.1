#!/bin/python3

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# 1. Add a new code file to your existing labs project and make it the startup file.



# 2. Copy the data string above into this file.



# 3. To extract information from this string, you'll need to split it by ',' as
# delimiter.


# Put the resulting List into a variable called grades.



# 4. Display the minimum value of the grades.



# 5. Display the maximum value of grades.



# 6. Test your code and check if the values are correct.


# Did your code display 100 for the minimum value and 99 for the maximum?


# But how can 100 be a minimum?



# 7. OK, as you've guessed it, we're dealing with a list of strings who just look like
# a List of numbers! That is why ‘100’ is less than ‘17’ because the first character
# '1' is the same but the second character '0' is less than the number '3'. So,
# you need to cast every element of a List of strings into a List of integers. This
# is a common task and a hard one to code, but the clever Python 3.0 gives us
# a tool called map to help us do this task.
# The map function was not covered in the lectures, so we'll cover this useful
# function here in this guided task.
# Just after splitting the string into a list of strings called grades, type:
# grades = list(map(int, grades))
# This line of code casts grades into a list of ints.


# 8. Now, run your code again. Does it give the right values for min and max (14
# and 100)?
# 2


# 9. Display the average of grades to two decimal points.
# Tip: use the sum(), len() and round() functions.


# 10. Import the statistics library.
# Tip: at the first line of your file type import statistics


# 11. Use the statistics' mean() function to get the average grade to two decimal
# places.
# Tip: use the statistics.mean() function


# 12. Display the median values using the statistics.median() function.
# The median is the value that appears in the middle of your dataset, after
# you’ve arranged the data in value order (i.e. lowest to highest, or highest to
# lowest).


# 13. Use the string.format() function to display the min, max, average, mean()
# and median values.
