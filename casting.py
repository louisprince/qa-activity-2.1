#!/bin/python3

# Cast a string to integer
some_number_in_a_string = "100"
another_number = 1 + int(some_number_in_a_string)
if another_number == 101:
    print("Correct")
else:
    print("Something went wrong")

# Cast a string to a float
another_number_in_a_string = "0.1"
yet_another_number = 0.2 + float(another_number_in_a_string)
if yet_another_number == 0.3:
    print("Correct")
else:
    print("Something went wrong")
    # It appears Python has the same deficiency that JavaScript has where floating point arithmetic doesn't work how you'd expect
    # 0.1 + 0.2 is in fact equal to 0.30000000000000004
