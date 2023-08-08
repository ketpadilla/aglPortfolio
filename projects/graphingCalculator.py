# TODO:
# Display the graph and a table of values for any "y=" equation input
# Solve a system of two equations without graphing
# Graph two equations and plot the point of intersection
# Given a, b and c in a quadratic equation, plot the roots and vertex



# LIBRARIES
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, pretty
from numpy import linspace, clip


# HELPER FUNCTIONS
def graph(functions, selectedOption):
    # ! SET INITIAL GRAPH DESIGN
    # Set axis lines to dashed black
    plt.plot([graphDimensions['xmin'], graphDimensions['xmax']], [0, 0], 'k--')
    plt.plot([0, 0], [graphDimensions['ymin'], graphDimensions['ymax']], 'k--')
    # Show grid with 0.5 spacing
    plt.xticks(range(graphDimensions['xmin'], graphDimensions['xmax']+1), fontsize=fontSize-10)
    plt.yticks(range(graphDimensions['ymin'], graphDimensions['ymax']+1), fontsize=fontSize-10)
    plt.grid(which='both', ls='--', lw=0.5, color='gray', alpha=0.5)
    # Set title
    plt.title(f"{options[selectedOption[0]].__name__.replace('_',' ').title()}", fontsize=fontSize)
    # ! SET AND PLOT COORDINATES
    # Initialize an array of x values
    xValues = linspace(graphDimensions['xmin'], graphDimensions['xmax'], 10*(graphDimensions['xmax'] - graphDimensions['xmin'])) 
    # Calculate coordinates and plot each function
    x = symbols('x')
    for i in range(len(functions)):
        # Initialize dictionary of coordinates, for y, convert the function to a lambda function then get the y values for the function
        coordinates = {'x': xValues, 'y': lambdify(x, functions[i], 'numpy')(xValues)}
        # Remove any values that are outside the graph dimensions
        mask = (coordinates['y'] >= graphDimensions['ymin']) & (coordinates['y'] <= graphDimensions['ymax'])
        coordinates['x'], coordinates['y'] = coordinates['x'][mask], coordinates['y'][mask]
        # Plot the function  
        plt.plot(*coordinates.values(), '-', label=f"y = {pretty(functions[i])}")
    # Show legend
    plt.legend(loc='upper left', fontsize=fontSize-5)
    # ! SHOW GRAPH
    plt.ion()
    plt.show()
    # ! EXIT GRAPH
    input("Press enter to exit graph.")
    plt.close()
    plt.ioff()
    return functions


def create_table_of_values(functions):
    # Initialize table
    ax = plt.subplot()
    ax.set_axis_off()
    # Initialize columns and rows
    columns, rows = ['x', 'y'], [[0,0]]
    # TODO: revise so that it works for any function
    # ? Maybe we show the table for each function separately then user must press enter to see the next one
    for a in range(1,10):
        rows.append([a, 3*a+2])
    plt.title("Testing")
    # Create table for each function
    # for i in range(len(functions)):
    #     # Set title
    #     plt.title(f"Table of Values for y = {pretty(functions[i])}", fontsize=fontSize)
    #     for a in range(1,10):
    #         rows.append([a, 3*a+2])
    plt.table(cellText=rows, colLabels=columns, cellLoc='center', loc='upper left')
    # Show table
    plt.show()
    return


def shade_area():
    return


# FUNCTIONS
def graph_linear_functions():
    x = symbols('x')
    # Get the number of functions to graph
    numberOfFunctions = int(input("How many functions would you like to graph? "))
    # Get the functions to graph
    functions = []
    for i in range(1, numberOfFunctions + 1):
        # Get string input for the function
        function = input(f"Enter function: y{i} = ")
        # Get coefficients (m and b)
        coefficients = [coefficient.strip() for coefficient in function.split('x')]
        m = int(coefficients[0]) if coefficients[0] and coefficients[0] != '-' else (-1 if coefficients[0] == '-' else 1)
        b = int(coefficients[1]) if len(coefficients) > 1 and coefficients[1] != '' else 0
        # Create then append the function to the list of functions
        functions.append(m * x + b)
    return functions


def solve_and_graph_system_of_equations():
    return print("Solving and graphing system of equations...")


def graph_two_equations_and_plot_point_of_intersection():
    return print("Graphing two equations and plotting point of intersection...")


def graph_a_quadratic_equation():
    return print("Graphing a quadratic equation...")


# INITIALIZE VARIABLES
options = {'a': graph_linear_functions, 'b': solve_and_graph_system_of_equations, 'c': graph_two_equations_and_plot_point_of_intersection, 'd': graph_a_quadratic_equation}
graphDimensions = {'xmin': -15, 'ymin': -15, 'xmax': 15, 'ymax': 15}
fontSize = max(9, (graphDimensions['xmax'] - graphDimensions['xmin']) / 2)


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
    functions = options.get(selectedOption[0], lambda: print("Error: Invalid option."))()
    # Create graph
    fig, ax = plt.subplots()
    equations = graph(functions, selectedOption)
    # Ask user if they want to create a table of values
    if input("Would you like to create a table of values? (y/n) ").lower() == 'y':
        create_table_of_values(equations)
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
    