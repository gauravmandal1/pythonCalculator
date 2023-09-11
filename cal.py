# Define functions for arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator loop
while True:
    # Display menu to the user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Take user input
    user_input = input(": ")

    # Check if user wants to quit
    if user_input == "quit":
        break

    # Check for valid operations
    if user_input not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid input")
        continue

    # Get numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if user_input == "add":
        print("Result:", add(num1, num2))
    elif user_input == "subtract":
        print("Result:", subtract(num1, num2))
    elif user_input == "multiply":
        print("Result:", multiply(num1, num2))
    elif user_input == "divide":
        print("Result:", divide(num1, num2))
