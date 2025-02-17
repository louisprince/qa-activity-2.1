chosen_number = int(input("Please input a whole number: "))
total = chosen_number

for i in range (chosen_number - 1, 1, -1):
    total = total * i

print(total)