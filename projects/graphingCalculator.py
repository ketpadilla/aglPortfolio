# LIBRARIES
import matplotlib.pyplot as plt
from sympy import symbols, lambdify, Eq, nonlinsolve, solve
from numpy import linspace, sqrt, array, max as npmax, min as npmin, maximum as npmaximum, minimum as npminimum
from re import findall, match, search
from sys import exit
from inspect import stack


# * HELPER FUNCTIONS
# CREATE GRAPH
def graph(functions, points, selectedOption):
    # ! FOR FUNCTIONS IN EQ FORM, SOLVE FOR Y AND CONVERT TO STR
    functions = [str(solve(eq, symbols('y'))[0]) if isinstance(eq, Eq) else eq for eq in functions]
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
    for i in range(len(functions)):
        # Calculate coordinates
        coordinates = generate_coordinates(functions[i], xValues)
        # Plot the function  
        plt.plot(*coordinates.values(), '-', label=f"y = {functions[i]}")
    # ! PLOT POINTS
    # Plot provided points
    [plt.plot(x, y, 'o', label=f'({x}, {y})') for x, y in points]
    # Show legend
    plt.legend(loc='upper left', fontsize=fontSize-5)
    # Check if function was called from shade_area(): if so, do not show graph immediately
    if stack()[1].function == 'shade_area': return functions
    # ! SHOW GRAPH
    show()
    # ! EXIT GRAPH
    input("Press enter to exit graph.")
    close()
    return functions


# GENERATE COORDINATES
def generate_coordinates(function, xValues):
    # Initialize symbol
    x = symbols('x')
    # ! Initialize dictionary of coordinates, for y, convert the function to a lambda function then get the y values for the function
    coordinates = {'x': xValues, 'y': lambdify(x, function, 'numpy')(xValues)}
    # Check if function was called from shade_area(): if so, do not show graph immediately
    if stack()[1].function == 'shade_area': return coordinates
    # ! Remove any values that are outside the graph dimensions
    mask = (coordinates['y'] >= graphDimensions['ymin']) & (coordinates['y'] <= graphDimensions['ymax'])
    coordinates['x'], coordinates['y'] = coordinates['x'][mask], coordinates['y'][mask]
    return coordinates


# CREATE TABLE OF VALUES
def create_table_of_values(functions):
    # Initialize an array of x values
    xValues = array(range(graphDimensions['xmin'], graphDimensions['xmax']+1))
    # Calculate coordinates and append to rows
    for i in range(len(functions)):
        # Initialize table
        ax = plt.subplot()
        ax.set_axis_off()
        # Initialize columns and rows
        columns, rows = ['x', 'y'], []
        # Calculate coordinates
        coordinates = generate_coordinates(functions[i], xValues)
        # ! Append coordinates to rows using list comprehension
        rows = [[round(coordinates['x'][j],0), round(coordinates['y'][j],0)] for j in range(len(coordinates['x']))]
        plt.title(f"Table of Values for y = {functions[i]}", fontsize=fontSize)
        table = ax.table(cellText=rows, colLabels=columns, cellLoc='center', loc='upper left')
        # Tighten layout and reduce width
        plt.tight_layout(rect=(0.2,0, 0.5, 1))
        # Adjust fontsize for table
        table.auto_set_font_size(False)
        table.set_fontsize(fontSize-8)
        # Show table
        show()
        # Prompt user to press enter to continue to next table or exit
        input("Press enter to continue to next table." if i < len(functions) - 1 else "Press enter to exit table.")
        close()
    return


# CONVERT STRING TO EQ
def convert_str_to_eq(function):
    sides = [findall(r'[-+]?\s*\d*\s*[xy]|[-+]?\s*\d+', side) for side in function.split('=')]
    parts = []
    for side in sides:
        components = [match(r'([-+]?\s*\d*)', component).group(1) for component in side]
        variables = [search(r'([xy])', component).group(1) if search(r'([xy])', component) else '' for component in side]
        side = [(coefficient + '*' + variable if coefficient not in ['', '+', '-'] and variable else coefficient + variable) for coefficient, variable in zip(components, variables)]
        # Append the side to the list of sides
        parts.append(side)
    x, y = symbols('x y')
    equation = Eq(eval(''.join(parts[0])), eval(''.join(parts[1])))
    return equation


# SOLVE SYSTEM
def solve_system():
    # Initialize list of functions
    functions = []
    # Get the functions to graph
    for i in range(1, 3):
        # Get string input for the function
        function = input(f"Enter equation (e.g., x + y = 2): ")
        # ! Convert string to a sympy equation
        equation = convert_str_to_eq(function)
        # ! Append the equation to the list of equations
        functions.append(equation)
    # Solve the system of equations
    intersection = nonlinsolve(functions, symbols('x y'))
    # End program if there is no solution
    if not intersection:
        print("No solution.")
        exit()
    return functions, intersection


# SHOW GRAPH
def show():
    return plt.ion(), plt.show()


# CLOSE GRAPH
def close():
    return plt.close(), plt.ioff()


# SHADE AREA
def shade_area(equations, points, selectedOption):
    # ! ASK USER FOR THE AREA TO SHADE
    # For more than 2 functions
    if len(equations) > 2: 
        return print("Program currently cannot shade areas for more than 2 functions.")
    # For linear and quadratic functions
    if len(equations) == 1:
        area = graphDimensions['ymax'] if input(f"Would you like to the shade above or below the line y = {equations[0]}? (a/b) ").lower() == 'a' else graphDimensions['ymin']
    # For systems of equations
    elif len(equations) == 2:
        area = input(f"Would you like to shade the area left (l), right (r), above (a), or below (b) the intersection of y = {equations[0]} and y = {equations[1]}? ").lower()
    # ! CREATE GRAPH
    equations = graph(equations, points, selectedOption)
    # ! FILL AREA
    # Initialize x values
    xValues = linspace(graphDimensions['xmin'], graphDimensions['xmax'], 10*(graphDimensions['xmax'] - graphDimensions['xmin'])) 
    # For linear and quadratic functions
    if len(equations) == 1:
        # Generate coordinates
        coordinates = generate_coordinates(equations[0], xValues)
        # ! DETERMINE AREA TO SHADE AND ENFORCE GRAPH BOUNDARIES
        if area == graphDimensions['ymax']:
            shadeArea = npminimum(npmaximum(coordinates['y'], graphDimensions['ymax']), graphDimensions['ymax'])
        elif area == graphDimensions['ymin']:
            shadeArea = npmaximum(npminimum(coordinates['y'], graphDimensions['ymin']), graphDimensions['ymin'])
        # ! ADJUST Y VALUES TO SHADE AREA AND ENFORCE GRAPH BOUNDARIES
        coordinates['y'] = npmaximum(npminimum(coordinates['y'], graphDimensions['ymax']), graphDimensions['ymin'])
        # Fill the specified area
        plt.fill_between(coordinates['x'], shadeArea, coordinates['y'], alpha=0.5)
    # For systems of equations
    else:
        # Generate coordinates
        coordinates1 = generate_coordinates(equations[0], xValues)
        coordinates2 = generate_coordinates(equations[1], xValues)
        # Convert coordinates to arrays
        coordinates1 = array(list(coordinates1.values()))
        coordinates2 = array(list(coordinates2.values()))
        # Set coordinates1 to the function with the higher coordinates on the left side
        if coordinates1[1][0] < coordinates2[1][0]:
            coordinates1, coordinates2 = coordinates2, coordinates1
        # ! DETEMINE AREA TO SHADE AND ENFORCE GRAPH BOUNDARIES
        if area == 'l': # left
            # Initialize shade start and end
            shadeStart = max(graphDimensions['ymin'], npmin(coordinates1[1]))
            shadeEnd = min(graphDimensions['ymax'], npmax(coordinates1[1]))
            # Fill the specified area
            plt.fill_between(xValues, npmaximum(npminimum(coordinates1[1], coordinates2[1]), shadeStart), npminimum(shadeEnd, npmaximum(coordinates1[1], coordinates2[1])), where=(coordinates1[1] > coordinates2[1]) & (xValues >= npmin(coordinates1[0])) & (xValues <= npmax(coordinates2[0])), alpha=0.5)
        elif area == 'r': # right
            # Initialize shade start and end
            shadeStart = max(graphDimensions['ymin'], npmin(coordinates1[1]))
            shadeEnd = min(graphDimensions['ymax'], npmax(coordinates2[1]))
            # Fill the specified area
            plt.fill_between(xValues, npmaximum(npminimum(coordinates1[1], coordinates2[1]), shadeStart), npminimum(shadeEnd, npmaximum(coordinates1[1], coordinates2[1])), where=(coordinates1[1] < coordinates2[1]) & (xValues >= npmin(coordinates1[0])) & (xValues <= npmax(coordinates2[0])), alpha=0.5)
        elif area == 'a': # above
            # Initialize shade area
            shadeArea = npmaximum(coordinates1[1], coordinates2[1])
            # Fill the specified area
            plt.fill_between(xValues, npminimum(shadeArea, graphDimensions['ymax']), graphDimensions['ymax'], alpha=0.5)
        elif area == 'b': # below
            # Initialize shade area
            shadeArea = npminimum(coordinates1[1], coordinates2[1])
            # Fill the specified area
            plt.fill_between(xValues, graphDimensions['ymin'], npmaximum(shadeArea, graphDimensions['ymin']), alpha=0.5)
    # ! SHOW GRAPH
    show()
    # ! EXIT GRAPH
    input("Press enter to exit graph.")
    return close()


# * FUNCTIONS
# GRAPH LINEAR FUNCTIONS
def graph_linear_functions():
    x = symbols('x')
    # Get the number of functions to graph
    numberOfFunctions = int(input("How many functions would you like to graph? "))
    # Get the functions to graph
    functions = []
    for i in range(1, numberOfFunctions + 1):
        # Get string input for the function
        function = input(f"Enter function: y{i} = ")
        # ! Get coefficients (m and b)
        coefficients = [coefficient.strip() for coefficient in function.split('x')]
        m = int(coefficients[0]) if coefficients[0] and coefficients[0] != '-' else (-1 if coefficients[0] == '-' else 1)
        b = int(coefficients[1]) if len(coefficients) > 1 and coefficients[1] != '' else 0
        # ! Create then append the function to the list of functions
        functions.append(m * x + b)
    return functions, [], True


# SOLVE AND GRAPH SYSTEM OF EQUATIONS
def solve_and_or_graph_system_of_equations():
    # ! Get functions and intersection
    functions, intersection = solve_system()
    # Print the solution
    print(f"The answer is x = {intersection.args[0][0]} and y = {intersection.args[0][1]}")
    # Ask user if they want to see the graph of the system of equations
    figure = True if input("Would you like to see the graph of the system of equations? (y/n) ").lower() == 'y' else False
    return functions, [[intersection.args[0][0], intersection.args[0][1]]], figure


# GRAPH TWO EQUATIONS AND PLOT POINT OF INTERSECTION
def graph_two_equations_and_plot_point_of_intersection():
    # ! Get functions and intersection
    functions, intersection = solve_system()
    # Print intersection
    print(f"The intersection is ({intersection.args[0][0]}, {intersection.args[0][1]})")
    return functions, [[intersection.args[0][0], intersection.args[0][1]]], True


# GRAPH A QUADRATIC EQUATION
def graph_a_quadratic_equation():
    # Initialize dictionary of values
    values = {'a': 0, 'b': 0, 'c': 0}
    # ! Ask for a, b, and c values (ax^2 + bx + c)
    print("Enter the values for ax^2 + bx + c")
    values = {key: int(input(f"Enter the value for {key}: ")) for key in values.keys()}
    # Create Eq function
    x = symbols('x')
    function = [values['a'] * x ** 2 + values['b'] * x + values['c']]
    # Print the equation
    print(f"The equation is y = {function[0]}")
    # ! Calculate the vertex
    vertex = [-values['b'] / (2 * values['a']), (4 * values['a'] * values['c'] - values['b'] ** 2) / (4 * values['a'])]
    # Print the vertex
    print(f"The vertex is ({vertex[0]}, {vertex[1]})")
    # Calculate disciminant
    discriminant = values['b'] ** 2 - 4 * values['a'] * values['c']
    # ! Calculate roots
    if discriminant > 0:
        root1, root2 = [(-values['b'] + sqrt(discriminant)) / (2 * values['a']),0.0], [(-values['b'] - sqrt(discriminant)) / (2 * values['a']),0.0]
        # Check if the vertex is a root before returning
        if vertex[0] == root1[0]:
            return function, [vertex, root2], True
        elif vertex[0] == root2[0]:
            return function, [vertex, root1], True
        return function, [vertex, root1, root2], True
    elif discriminant == 0:
        root = [-values['b'] / (2 * values['a']),0.0]
        # Print the root
        print(f"The root is ({root[0]}, {root[1]})")
        # Check if the vertex is a root before returning
        return (function, [vertex], True) if vertex[0] == root[0] else (function, [vertex, root], True)
    # Return values
    print("There are no real roots")
    return function, [vertex], True


# INITIALIZE VARIABLES
options = {'a': graph_linear_functions, 'b': solve_and_or_graph_system_of_equations, 'c': graph_two_equations_and_plot_point_of_intersection, 'd': graph_a_quadratic_equation}
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
    # Prompt user unsupported inputs
    print("\nFractions and decimals are not supported. Please enter integers only.")
    # Call the function based on the user's choice
    
    functions, points, figure = options.get(selectedOption[0], lambda: print("Error: Invalid option."))()
    if figure == False: return
    # ! Create graph
    fig, ax = plt.subplots()
    equations = graph(functions, points, selectedOption)
    # Ask user if they want to create a table of values
    if input("Create a table of values? (y/n) ").lower() == 'y': create_table_of_values(equations)
    # If provided equations > 1, ask user if they want to shade the area between the two equations
    if input("Shade an area of the graph? (y/n) ").lower() == 'y': shade_area(equations, points, selectedOption)
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
    