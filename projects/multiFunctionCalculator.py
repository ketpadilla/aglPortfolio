# LIBRARIES
from sympy import sqrt, symbols, Eq, sympify, pretty
from sympy.solvers import solve
from re import sub


# * OPERATIONS
# ADDITION
def add():
    # Get numbers from user and convert them to integers
    inputs = [int(i) for i in input("Enter numbers to add, separate each number with a space: ").split()]
    # Add the numbers
    return print(f"The sum of {' + '.join(map(str, inputs))} is {sum(inputs)}")


# SUBTRACTION
def subtract():
    # Get numbers from user and convert them to integers
    inputs = [int(i) for i in input("Enter numbers to subtract, separate each number with a space: ").split()]
    # Subtract the first number by the rest of the numbers
    return print(f"The difference of {' - '.join(map(str, inputs))} is {inputs[0] - sum(inputs[1:])}")


# MULTIPLICATION
def multiply():
    # Get numbers from user
    inputs = [int(i) for i in input("Enter numbers to multiply, separate each number with a space: ").split()]
    # Set the product to 1
    product = 1
    # Multiply the product by each number
    for number in inputs:
        product *= number
    # Print the product
    return print(f"The product of {' * '.join(map(str, inputs))} is {product}")


# DIVISION
def divide():
    # Get numbers from user
    inputs = [int(i) for i in input("Enter numbers to divide, separate each number with a space: ").split()]
    # Set the quotient to the first number
    quotient = inputs[0]
    # Divide the quotient by the rest of the numbers
    for number in inputs[1:]:
        quotient /= number
    # Print the quotient
    return print(f"The quotient of {' / '.join(map(str, inputs))} is {round(quotient, 2)}")


# DETECT PRIME NUMBERS
def detect_prime():
    # Get number from user
    number = int(input("Enter a number to check if it is prime: "))
    # Check if number is prime or composite
    numberType = "prime" if not any(number % num == 0 for num in range(2, number)) else "composite"
    # Print result
    return print(f"{number} is a {numberType} number.")


# GENERATE PRIME FACTORS
def generate_prime_factors():
    # Get number from user
    number = int(input("Enter a number to generate its prime factors: "))
    # Generate prime factors
    primeFactors = [num for num in range(1, number+1) if number % num == 0]
    # Print factors
    return print(f"The prime factors of {number} are {primeFactors}")


# SIMPLIFY SQUARE ROOTS
def generate_square_roots():
    # Get number from user
    number = int(input("Enter a number to simplify its square root: "))
    # Perform square root and print in pretty format
    return print(f"The square root of {number} is {pretty(sqrt(number))}")


# SOLVE EQUATIONS
def solve_equations():
    # Get the equation from user
    equation = problem = input("Enter an equation to solve: ")
    # Check if the equation is valid (contains only one equal sign)
    if "=" not in equation or equation.count("=") > 1:
        return print("Invalid equation. Please try again.")
    # Extract variables from the equation
    variables = {symbols(variable) for variable in set(equation) if variable.isalpha()}
    # Format the equation
    equation = sub(r'(\d)([a-zA-Z])', r'\1*\2', equation).replace(" ", "").replace("^", "**").split("=")
    # If there are multiple variables, ask the user which one to solve for
    if len(variables) > 1:
        variable = input(f"Variables: {', '.join(map(str, variables))}\nEnter a variable to solve for: ")
        if variable not in map(str, variables):
            return print("Invalid variable.")
    else:
        # If there's only one variable, automatically select it
        variable = next(iter(variables))
    # Solve the equation
    answer = solve(Eq(sympify(equation[0]), sympify(equation[1])), variable)    
    # Check if there are any solutions
    if len(answer) >= 1:
        # Print the answer(s)
        print(f"The solution{'s' if len(answer) > 1 else ''} to {problem} {'are:' if len(answer) > 1 else 'is:'}")
        for ans in answer:
            # Iterate through each answer
            print(f" {variable} = {pretty(ans)}")
        return
    # If no solutions are found, print an error message
    return print("No solutions found.")


# INITIALIZE GLOBAL VARIABLES
options = {'a': add,'b': subtract,'c': multiply,'d': divide, 'e': detect_prime, 'f': generate_prime_factors, 'g': generate_square_roots, 'h': solve_equations}


# MENU SELECTION
def menu():
    global options
    while True:
        # Print the options
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selectedOption = input("\nSelect an option (only enter the letter): ")
        # Validate the user's choice
        if selectedOption.replace('.','').lower() in options:
            selectedOption = selectedOption.replace('.','').lower() # ! ensure option is lowercase and without a period
            return selectedOption, options[selectedOption]
        print(f"\n {selectedOption} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main():
    # Menu selection
    selectedOption = menu()
    # Call the function based on the user's choice
    options.get(selectedOption[0], lambda: print("Error: Invalid option."))()
    return


# * RUN PROGRAM
main()
