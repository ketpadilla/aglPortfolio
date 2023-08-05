# LIBRARIES
import matplotlib.pyplot as plt
...


# FUNCTIONS
def graph(): # ! Sample
    return 


# INITIALIZE GLOBAL VARIABLE
options = {'a': graph}


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
if __name__ == "__main__":
    main()
    