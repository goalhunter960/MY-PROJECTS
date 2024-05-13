import math

# Define the functions for calculator operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def solve_equation(equation):
    # Evaluates a mathematical expression and returns the result
    try:
        result = eval(equation)
        return result
    except Exception as e:
        return str(e)

# Chatbot interaction loop
print("Hi! I am an advanced chatbot. How can I assist you today?")

while True:
    user_input = input("Enter your question or mathematical expression (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # Check if the user input is a mathematical expression
    if any(char.isdigit() for char in user_input):
        result = solve_equation(user_input)
        print("Result: ", result)
    else:
        print("Sorry, I can only solve mathematical problems. Please provide a valid mathematical expression.")
