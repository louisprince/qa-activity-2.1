#!/bin/python3

# Via print statement
print("Hello world!")

# Via parameter input
message = "Hello world!"
print(message)


# Via function return
def hello(input: str) -> str:
    return f"Hello {input}!"


print(hello("world"))

# Via user input
user_input = ""
while user_input != "world":
    user_input = input("Please enter the word \"world\": ")
    if user_input == "world":
        print(hello(user_input)) # Might as well use that function from before
    else:
        print("Incorrect input, please try again!")
