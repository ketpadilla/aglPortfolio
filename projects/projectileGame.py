# LIBRARIES
import matplotlib.pyplot as plt
from random import randint

# INITIALIZE GLOBAL VARIABLES
score = 0
xmin = ymin = -10
xmax = ymax = 10


# INITIALIE GRAPH
fig, ax = plt.subplots()


# FUNCTIONS
# Create graph
def graph(x, y):
    # Set axis lines to blue
    plt.plot([xmin,xmax],[0,0],'b')
    plt.plot([0,0],[ymin,ymax],'b')
    # Plot point
    plt.plot(x,y,'ro')
    # Show grid
    plt.grid()
    # Set title
    plt.title("Projectile Game")
    # Show graph
    plt.show()
    return


# Check if ... 
def check():
    # TODO: for initial velocity
    ...
    return score


# TODO: graph animation


# * MAIN FUNCTION
def main():
    # Initialize global variables
    global xmin, ymin, xmax, ymax
    # Set starting point
    x = y = 0
    # TODO: randomize function for height and wall location
    # Create graph
    graph(x, y)
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
