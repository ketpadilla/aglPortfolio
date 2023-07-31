## LINEAR FUNCTIONS - functions that can be written in the form f(x) = mx + b where m and b are real numbers and m ≠ 0.

# --- #

# * SLOPES - the steepness of a line.
# FORMULA: m = (y2 - y1) / (x2 - x1)
# SLOPE INTERCEPT FORM: y = mx + b; an equation of a line with slope m and y-intercept b.

# EXAMPLE:
# Initize variables
x1 = 1
y1 = 7
x2 = 2
y2 = 10
# Calculate slope
m = (y2 - y1) / (x2 - x1)
# Print slope
print("slope = ", m)
# Calculate y-intercept
b = y1 - m * x1
# Print slope intercept form
print(f"y = {m}x + {b}")

# GRAPH OF EXAMPLE (matplotlib):
import matplotlib.pyplot as plt
# Initialize x and y min and max values
xmin = -10
xmax = 10
ymin = -10
ymax = 10
# Initialize lines for graph
y3 = m * xmin + b
y4 = m * xmax + b
# Setup graph
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')
# Plot line
plt.plot([xmin, xmax], [y3, y4], 'r')
# Show graph
plt.show()

# --- #

# ! Usage center around solving for the missing value then graphing the completed equation.
# Libraries to use: sympy, sympy.solvers, matplotlib, & numpy