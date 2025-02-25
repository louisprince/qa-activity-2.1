#!/bin/python3

operator = input("Enter an operator: ")
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))  
dangerous = eval(f"lambda a, b: a {operator} b")
print(dangerous(first, second))
