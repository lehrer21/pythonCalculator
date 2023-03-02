# A simple calculator

ADDITION_SELECTION = 1
SUBTRACTION_SELECTION = 2
MULTIPLICATION_SELECTION = 3
DIVISION_SELECTION = 4


# Function to add two numbers
def add(n1, n2):
    return n1 + n2


# Function to subtract two numbers
def subtract(n1, n2):
    return n1 - n2


# Function to multiply two numbers
def multiply(n1, n2):
    return n1 * n2


# Function to divide two numbers
def divide(n1, n2):
    return n1 / n2


print("Calculator Menu -\n" \
      "1. Add two numbers -\n" \
      "2. Subtract two numbers -\n" \
      "3. Multiply two numbers -\n" \
      "4. Divide two numbers -\n")

# Takes user input in the form of a string to select the operation.
select = input("Which operation would you like to carry out? Pick a number 1-4: ")

# Takes user input in the form of a string and converts it to an integer to carry out the operation.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Prints and carries out the chosen operation and prints the output.
if select == ADDITION_SELECTION:
    print(number1, " +", number2, "=",
          add(number1, number2))

elif select == SUBTRACTION_SELECTION:
    print(number1, "-", number2, "=",
          subtract(number1, number2))

elif select == MULTIPLICATION_SELECTION:
    print(number1, "*", number2, "=",
          multiply(number1, number2))

elif select == DIVISION_SELECTION:
    print(number1, "/", number2, "=",
          divide(number1, number2))
else:
    print("Invalid input!")
