from calculator import Calculator

def main():
    calculator = Calculator()
    result = None

    while result is None:
        option = get_option()
        
        if option == "quit" or option == "q":
            exit(0)

        first, second = get_numbers()
        result = calculate(calculator, option, first, second)

        if result == ValueError: 
            input("Invalid input. Press enter to try again...")
            result = None

    print(f"Result: {result}")   

def get_option():
    option = input(
        "Please choose an option:\n" +
        "add (a)\n" +
        "subtract (s)\n" +
        "multiply (m)\n" +
        "divide (d)\n" +
        "quit (q)\n")

    return option.lower()

def get_numbers():
    first = None
    second = None

    while first == None:
        try:
            first = float(input("Enter the first number: "))
        except ValueError:
            print("You must input a number!")
            continue

    while second == None:
        try:
            second = float(input("Enter the second number: ")) 
        except ValueError:
            print("You must input a number!")
            continue
    
    return first, second

def calculate(calculator: Calculator, option: str, first: float, second: float):
    match option:
        case "add": return calculator.add(first, second)
        case "a": return calculator.add(first, second)
        case "subtract": return calculator.subtract(first, second)
        case "s": return calculator.subtract(first, second)
        case "multiply": return calculator.multiply(first, second)
        case "m": return calculator.multiply(first, second)
        case "divide": return calculator.divide(first, second)
        case "d": return calculator.divide(first, second)
        case _: return ValueError

main()