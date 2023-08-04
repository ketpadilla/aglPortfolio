## GRAPHING SYSTEMS OF EQUATIONS

# --- #

# * EXAMPLE
# Import libraries
import numpy as np
import matplotlib.pyplot as plt
# Initialize minimum and maximum values for x and y
xmin = ymin = -10
xmax = ymax = 10
# Define how many points to plot
points = 10*(xmax-xmin)
# Define the array of x values
x = np.linspace(xmin, xmax, points)
# Initialize graph
fig, ax = plt.subplots()
# Set window size
plt.axis([xmin, xmax, ymin, ymax])
# Show Axis in blue
plt.plot((xmin, xmax), (0, 0), 'b-')
plt.plot((0, 0), (ymin, ymax), 'b-')
# ! Line 1
# Define the equation
y1 = 3*x
# Plot the line
plt.plot(x, y1, label='y1')
# ! Line 2
# Define the equation
y2 = x**3
# Plot the line
plt.plot(x, y2, label='y2')
# Show grid
plt.grid(True)
# Show legend
plt.legend(loc='upper left')
# Show figure
plt.show()

# --- #

# * SHADING REGIONS
# Set graph, window size, and axes
fig, ax = plt.subplots()
plt.axis([xmin, xmax, ymin, ymax])
plt.plot((xmin, xmax), (0, 0), 'b-')
plt.plot((0, 0), (ymin, ymax), 'b-')
# Line 1
y1 = x+6
plt.plot(x, y1, '-')
# ! Fill between
plt.fill_between(x, y1, ymax, facecolor='red')
# Line 2
y2 = x-1
plt.plot(x, y2)
plt.fill_between(x, y1, y2, facecolor='green')
# Line 3
y3 = x-4
plt.plot(x, y3)
plt.fill_between(x, y3, y2, facecolor='blue')
# Show graph
plt.show()

# --- #

# * INTERACTIVE GRAPHS
# ! refer to https://colab.research.google.com/drive/1m5oG62NzUHRzBghGCPRfr1SzvbywRWPV?usp=sharing
# ! uses: from ipywidgets import interact (pip install ipywidgets)

# --- #

# * GRAPHING WEATHER DATA
# ! refer to https://colab.research.google.com/drive/1m5oG62NzUHRzBghGCPRfr1SzvbywRWPV?usp=sharing
# ! uses: from datetime import datetime (pip install datetime)
# ! uses: from meteostat import Point, Daily (pip install meteostat)

# --- #
