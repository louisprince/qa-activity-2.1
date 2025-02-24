#!/bin/python3

def main():
    result = None
    while result is None:
        option = input("Please enter an operator: ")
        first = int(input("Please enter the first number: "))
        second = int(input("Please enter the second number: "))  
        result = calculate(option, first, second)
        if result == ValueError: 
            input("Invalid input. Please press enter to try again...\n")
            result = None
    print(f"Result: {result}\n")

def calculate(option: str, first: int, second: int):
    match option:
        case "+": return (lambda a, b: a + b)(first, second)
        case "-": return (lambda a, b: a - b)(first, second)
        case "*": return (lambda a, b: a * b)(first, second)
        case "/": return (lambda a, b: a / b)(first, second)
        case _: return ValueError

main()
