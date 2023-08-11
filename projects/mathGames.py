# LIBRARIES
import matplotlib.pyplot as plt
from random import randint
from numpy import linspace, sqrt, sin, cos, tan, arctan


# * HELPER FUNCTIONS


# * FUNCTIONS
# SCATTER PLOT GAME
def scatter_plot():
    return print("scatter plot")


# ALGEBRA PRACTICE GAME
def algebra_practice():
    return print("algebra practice")


# PROJECTILE GAME
def projectiles():
    return print("projectiles")


# INITIALIZE VARIABLES
options = {'a': scatter_plot, 'b': algebra_practice, 'c': projectiles}
graphDimensions = {'xmin': -15, 'ymin': -15, 'xmax': 15, 'ymax': 15}
fontSize = max(9, (graphDimensions['xmax'] - graphDimensions['xmin']) / 2)


# MENU SELECTION
def menu(options):
    global graphDimensions, fontSize
    while True:
        # Print the options
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selectedOption = input("\nSelect a game to play (only enter the letter): ")
        # Validate the user's choice
        if selectedOption.replace('.','').lower() in options:
            selectedOption = selectedOption.replace('.','').lower() # ! ensure option is lowercase and without a period
            return selectedOption, options[selectedOption]
        print(f"\n {selectedOption} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main(options):
    # Menu selection
    selectedOption = menu(options)
    # Call the function based on the user's choice
    options.get(selectedOption[0], lambda: print("Error: Invalid option."))()
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main(options)
    