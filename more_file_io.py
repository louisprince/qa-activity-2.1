import sys

# File input
with open("input.txt", "w") as file:
    file.write("   42\n")  # Test input with leading/trailing spaces

# Reading input from a file
with open("input.txt", "r") as file:
    sys.stdout.write("Reading from file: ")
    sys.stdout.flush()
    file_input = file.readline().strip()
    print(file_input)