# TODO:
# Display the graph and a table of values for any "y=" equation input
# Solve a system of two equations without graphing
# Graph two equations and plot the point of intersection
# Given a, b and c in a quadratic equation, plot the roots and vertex



# LIBRARIES
import matplotlib.pyplot as plt
from sympy import symbols
from numpy import linspace
...


# INITIALIZE GRAPH
fig, ax = plt.subplots()


# HELPER FUNCTIONS
def set_graph_design():
    return


def create_table_of_values():
    return


def shade_area():
    return


# FUNCTIONS
def graph_linear_functions(): # ! Sample
    return print("Graphing functions...")


def solve_and_graph_system_of_equations():
    return print("Solving and graphing system of equations...")


def graph_two_equations_and_plot_point_of_intersection():
    return print("Graphing two equations and plotting point of intersection...")


def graph_a_quadratic_equation():
    return print("Graphing a quadratic equation...")


# INITIALIZE VARIABLES
options = {'a': graph_linear_functions, 'b': solve_and_graph_system_of_equations, 'c': graph_two_equations_and_plot_point_of_intersection, 'd': graph_a_quadratic_equation}
graphDimensions = {'xmin': -15, 'ymin': -15, 'xmax': 15, 'ymax': 15}
fontSize = max(9, 2 * min((graphDimensions['xmax'] - graphDimensions['xmin']), (graphDimensions['ymax'] - graphDimensions['ymin'])))


# MENU SELECTION
def menu():
    global options, graphDimensions, fontSize
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
    