# A simple text-based calculator
# An art.py module containing ASCII art for the logo
from art import logo

ADDITION_SELECTION = "1"
SUBTRACTION_SELECTION = "2"
MULTIPLICATION_SELECTION = "3"
DIVISION_SELECTION = "4"


# This function takes in two variables to add them.
def add(n1, n2):
    return n1 + n2


# This function takes in two variables and subtracts the second from the first.
def subtract(n1, n2):
    return n1 - n2


# This function takes in two variables and multiplies them.
def multiply(n1, n2):
    return n1 * n2


# This function takes in two variables and divides the first by the second.
def divide(n1, n2):
    return n1 / n2


# The directions for the user are displayed using simple print statements along with the logo.
print(logo)
print("Calculator Menu")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Divide two numbers")

# Takes user input in the form of a string to select the operation.
select = input("Which operation would you like to carry out? Pick a number 1-4: ")

# Takes user input in the form of a string and converts it to an integer to carry out the operation.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Prints and carries out the chosen operation and prints the output.
if select == ADDITION_SELECTION:
    print(f"{number1} + {number2} = {add(number1, number2)}")

elif select == SUBTRACTION_SELECTION:
    print(f"{number1} - {number2} = {subtract(number1, number2)}")

elif select == MULTIPLICATION_SELECTION:
    print(f"{number1} * {number2} = {multiply(number1, number2)}")

elif select == DIVISION_SELECTION:
    print(f"{number1} / {number2} = {divide(number1, number2)}")
else:
    print("Invalid input!")
