## SOLVING SYSTEMS OF EQUATIONS

# --- #

# * EXAMPLE
# Import libraries
from sympy import *
# Define equations
x, y = symbols('x y')
eq1 = 2*x + y - 1
eq2 = x - 2*y + 7
# Solve the system of equations
solution = linsolve([eq1, eq2], (x, y))
x, y = next(iter(solution))
# Print the solution
print(f"The solution is x = {x} and y = {y}")

# --- #

# * EXAMPLE WITH GRAPH
x, y = symbols('x y')
eq1, eq2 = -x**2 - y + 10, 2*x**2 - 2*y - 4
# ! Solve the system of equations (linear and non-linear)
solution = nonlinsolve([eq1, eq2], (x, y))
# ! Print the solution
for a, b in solution:
    print(f"The solution is x = {pretty(a)} and y = {pretty(b)}")
# ! Convert equations to sympy format
eq1, eq2 = Eq(eq1,0), Eq(eq2,0)
# ! Solve for y in terms of x
y1 = solve(eq1, y)
y2 = solve(eq2, y)
# Print the solutions
print(f"The solutions are y = {y1} and y = {y2}")
# ! Plot the equations
x = symbols('x')
xmin, xmax = -10, 10
plot(y1[0], y2[0], (x, xmin, xmax))
    
# --- #

# * GRAPHING QUADRATIC EQUATIONS
# ! Import libraries
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, e
# ! Initialize equation
a, b, c = 1, 5, 6
# ! Calculate the vertex
vx, vy = -b/(2*a), -(b**2 - 4*a*c)/(4*a)
# ! Calculate discriminant
d = b**2 - 4*a*c
# ! Calculate the roots
if d > 0:
    x1, x2 = (-b + sqrt(d))/(2*a), (-b - sqrt(d))/(2*a)
    print(f"The roots are {x1} and {x2}")
elif d == 0:
    x1 = -b/(2*a)
    print(f"The root is {x1}")
else:
    print("There are no real roots")
# Set graph
xmin, xmax = -10, 10
ymin, ymax = -10, 10
points = 10*(xmax - xmin)
x = np.linspace(xmin, xmax, points)
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'b')
plt.plot([0, 0], [ymin, ymax], 'b')
# ! Plot the quadratic equation
y = a*x**2 + b*x + c
plt.plot(x, y)
# ! Plot vertex and roots
plt.plot(vx, vy, 'ro')
if d > 0:
    plt.plot([x1, x2], [0,0], 'ro')
else: 
    plt.plot(x1, 0, 'ro')
# Show graph
plt.show()

# --- #

# * PYTHON NOTATIONS OF EQUATIONS
x, y = 4, symbols('y') # ! Sample values
# y = x
y = x
# y = x^2
y = x**2
# y = |x|
y = abs(x)
# y = √x
y = np.sqrt(x)
# y = x^(1/3)
y = np.cbrt(x)
# y = ⌊x⌋
y = np.floor(x)
# y = 2^x
y = 2**x
# y = e^x
y = e**2
# y = ln(x)
y = np.log(x)
# y = log_2(x)
y = np.log2(x)
# y = log(x)
y = np.log10(x)

# --- #