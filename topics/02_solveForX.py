## SOLVING FOR X

# --- #

# * SYMPY - a Python library for symbolic mathematics.
from sympy import symbols, Eq 
from sympy.solvers import solve

# Initialize x as a symbol.
x = symbols('x')
# Initialize the equation.
equation = Eq(2*x + 3, 5) # ! The same as: 2x + 3 = 5
# Solve for x.
solution = solve(equation)
# Print the solution.
print(f"Equation 1: {equation} -> x = {solution[0]}")

# --- #

# * SOLVING FOR THE EQUATION WHERE THE VARIABLE HAS MULTIPLE SOLUTIONS
# Initialize x as a symbol.
x = symbols('x')
# Initialize the equation.
equation = Eq(x**2 - 4, 0) # ! The same as: x^2 - 4 = 0
# Solve for x.
solution = solve(equation)
# Print the solution.
print(f"Equation 2: {equation} -> x = {solution}")

# --- #

# * SOLVING FOR THE EQUATION OF ONE VARIABLE
from sympy import var 
# Initialize x and y as symbols.
x, y = var('x y')
# Initialize the equation.
equation = Eq(2*x + 3*y, 5) # ! The same as: 2x + 3y = 5
# Solve for x.
solution = solve(equation, x)
# Print the solution.
print(f"Equation 2: {equation} -> x = {solution[0]}")

# --- #

# * EXPANDING AND FACTORING
from sympy import expand, factor
# Initialize x as a symbol.
x = symbols('x')
# Initialize the equation.
equation = (x + 1)**2 # ! The same as: (x + 1)^2
# Expand the equation.
expanded = expand(equation)
# Print the expanded equation.
print(f"Equation 3: {equation} -> Expanded: {expanded}")
# Factor the equation.
factored = factor(expanded)
# Print the factored equation.
print(f"Equation 3: {expanded} -> Factored: {factored}")

# --- #

# !  Library may be used to solve for proportions dynamically.
# * Concept: 
# Ask user for the fractions; put x for the missing value. Then, find x within the two inputs with another library (so that user does not need to put * inbetween x). Then, setup fraction and symbol and solve for x