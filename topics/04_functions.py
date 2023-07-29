## FUNCTIONS
# In mathematics - a relation between a set of inputs and a set of outputs
# In programming - a block of code that performs a specific task

# --- #

# * FUNCTIONS IN MATHEMATICS
print("x \t y") # Print the table header
for x in range(5): # Loop through the values 0 to 4
    y = 4*x + 3  # ! The function
    print(x, "\t", y)

print("") # --- #

# * FUNCTIONS IN PROGRAMMING
# ! Define function
def f(x): 
    return 4*x + 3
print("x \t y") # Print the table header
# Call function
for x in range(5):
    print(x, "\t", f(x))

# --- #

## GRAPHING FUNCTIONS
import matplotlib.pyplot as plt # ! pip install matplotlib

# --- #

# * Blank Graph
fig, ax = plt.subplots() # Create a figure containing a single axes
ax.set_title("Blank Graph") # Set title
plt.show() # Display the figure

# --- #

# * Define dimensions of graph
fig, ax = plt.subplots()
plt.axis([0, 5, 0, 20]) # ! [xmin, xmax, ymin, ymax]
ax.set_title("Graph with Dimenstions") # Set title
plt.show() # Display the figure

# --- #

# * Display axis lines and better way to define dimensions
# ! Initialize variables
xmin = -5
xmax = 5
ymin = -20
ymax = 20
# Create graph
fig, ax = plt.subplots()
# ! Define dimensions
plt.axis([xmin, xmax, ymin, ymax])
# ! Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
ax.set_title("Graph with Axis Lines") # Set title
plt.show() # Display the figure

# --- #

# * Plot a point
# Initialize variables
xmin = -5
xmax = 5
ymin = -20
ymax = 20
# Create graph
fig, ax = plt.subplots()
# Define dimensions
plt.axis([xmin, xmax, ymin, ymax])
# Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
# ! Plot a point
plt.plot(2, 7, 'ro') # red point
ax.set_title("Graph with a Point") # Set title
plt.show() # Display the figure


# --- #

# * Plot multiple points at once using a loop
# ! Define function
def f(x):
    return 4*x + 3
# Initialize variables
xmin = -5
xmax = 5
ymin = -20
ymax = 20
# Create graph
fig, ax = plt.subplots()
# Define dimensions
plt.axis([xmin, xmax, ymin, ymax])
# Display axis lines
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
ax.set_title("Graph with Multiple Points") # Set title
for x in range(-5, 6):
    plt.plot(x, f(x), 'ro') # red point
plt.show() # Display the figure

# --- #

# * Plot a line using an array of x values
# ! Import numpy
import numpy as np
# ! Initialize variables
xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin) # ! Number of points to plot
x = np.linspace(xmin, xmax, points) # ! Create array of x values to plot
# Create graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # Define dimensions
# Display axis lines
plt.plot([xmin,xmax],[0,0],'b')
plt.plot([0,0],[ymin,ymax], 'b')
# ! Plot line
y = 2*x +1
plt.plot(x,y, 'pink')
ax.set_title("Graph with Line") # Set title
plt.show() # Show graph

# --- #

# * Other customizations 
# Initialize variables
xmin = -10
xmax = 10
ymin = -10
ymax = 10
points = 2*(xmax-xmin)
x = np.linspace(xmin, xmax, points)
# Create graph
fig, ax = plt.subplots()
plt.axis([xmin,xmax,ymin,ymax]) # window size
plt.plot([xmin,xmax],[0,0],'b') # blue x axis
plt.plot([0,0],[ymin,ymax], 'b') # blue y axis
# ! Set axis labels, title, and grid
ax.set_xlabel("x values")
ax.set_ylabel("y values")
ax.set_title("Custom Graph")
ax.grid(True)
# ! Set axis ticks
ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 1))
# Plot line
y = 2*x +1
plt.plot(x,y, label='y=2x+1') # ! Add label for legend
plt.plot([4],[6], 'ro', label='point') # ! Add label for legend
plt.plot(x,3*x, label='steeper line') # ! Add label for legend
plt.legend() # ! Display legend
plt.show()

# --- #

# ! Summary of functions used in graphing
# * Creating graph
# fig, ax = plt.subplots()

# * Setting axis dimensions
# plt.axis([xmin,xmax,ymin,ymax])
# * Displaying axis lines
# plt.plot([xmin,xmax],[0,0],'color')
# plt.plot([0,0],[ymin,ymax], 'color')

# * Setting axis labels, title, and grid
# ax.set_xlabel("x values")
# ax.set_ylabel("y values")
# ax.set_title("Graph Name")
# ax.grid(True)

# * Setting axis ticks
# ax.set_xticks(np.arange(xmin, xmax, space))
# ax.set_yticks(np.arange(ymin, ymax, space))

# * Plotting points and lines with labels
# ! Line color will automatically be different from points and other lines if not specified
# ! Color options: b, g, r, c, m, y, k, w
# plt.plot(x,y, label='name')
# plt.plot([x-value],[y-value], 'color', label='name')

# * Showing legend and graph
# plt.legend()
# plt.show()