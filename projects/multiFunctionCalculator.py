# LIBRARIES


# OPERATIONS
def add():
    inputs = [int(i) for i in input("Enter numbers to add, separate each number with a space: ").split()]
    return print(f"The sum of {' + '.join(map(str, inputs))} is {sum(inputs)}")


def subtract():
    inputs = [int(i) for i in input("Enter numbers to subtract, separate each number with a space: ").split()]
    return print(f"The difference of {' - '.join(map(str, inputs))} is {inputs[0] - sum(inputs[1:])}")


def multiply():
    inputs = [int(i) for i in input("Enter numbers to multiply, separate each number with a space: ").split()]
    product = 1
    for number in inputs:
        product *= number
    return print(f"The product of {' * '.join(map(str, inputs))} is {product}")


def divide():
    inputs = [int(i) for i in input("Enter numbers to divide, separate each number with a space: ").split()]
    quotient = inputs[0]
    for number in inputs[1:]:
        quotient /= number
    return print(f"The quotient of {' / '.join(map(str, inputs))} is {quotient}")


# TODO: add other operations


# INITIALIZE GLOBAL VARIABLES
options = {'a': add,'b': subtract,'c': multiply,'d': divide}


# MENU SELECTION
def menu():
    global options
    while True:
        # Print the options
        for key, value in options.items():
            print(f"{key}. {value.__name__}")
        # Get the user's choice
        selectedOption = input("\n Select an option (only enter the letter): ")
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


