## QUADRATICS

# --- #

# * SOLVING QUADRATIC EQUATIONS
# ! Initialising coefficients (ax^2 + bx + c = 0)
a, b, c = 1, 2, -8
# Show equation
print(f"{a}x^2 + {b}x + {c} = 0")
# Calculate Vertex
vx, vy = -b/(2*a), (4*a*c - b**2)/(4*a)
# Calculate Discriminant
d = b**2 - 4*a*c
# Calculate Roots
if d >= 0:
    x1, x2 = (-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a)
    print(f"Roots: {x1}, {x2}")
else:
    print("No real roots")

# --- #

# * GRAPHING QUADRATIC EQUATIONS
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
# ! Use the same coefficients as above for sample
# Initialize variables
xmin, ymin, xmax, ymax = -10, -10, 10, 10
points = 10*(xmax - xmin)
x = np.linspace(xmin, xmax, points)
# Initialie graph
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], color="b")
plt.plot([0, 0], [ymin, ymax], color="b")
# ! Graph equation
y = a*x**2 + b*x + c
plt.plot(x, y, color="r")
# ! Graph vertex
plt.plot(vx, vy, marker="o", color="g")
# ! Graph roots
if d >= 0:
    plt.plot(x1, 0, marker="o", color="g")
    plt.plot(x2, 0, marker="o", color="g")
# Show graph
plt.show()

# --- #
