# LIBRARIES
import matplotlib.pyplot as plt
from random import randint
import numpy as np

# INITIALIZE VARIABLES
# Initialize score and launch angle
score = 0
launchAngle = 45
# Initialize wall dimensions
distance = randint(5, 15)
wallDimensions = {'x': [5, 5], 'y': [0, 10]}
# Initialize graph dimensions
graphDimensions = {'xmin': -1, 'ymin': -1, 'xmax': wallDimensions['x'][0] + 3, 'ymax': wallDimensions['y'][1] + 3}
# Initialize font size
fontSize = max(9, 2 * min((graphDimensions['xmax'] - graphDimensions['xmin']) / distance, (graphDimensions['ymax'] - graphDimensions['ymin']) / distance))


# INITIALIE GRAPH
fig, ax = plt.subplots()


# FUNCTIONS
def trajectory(graphDimensions, wallDimensions, launchAngle):
    gravity = 9.8
    maxHeight = wallDimensions['y'][1]
    distance = wallDimensions['x'][0]
    # Calculate the number of points to plot given graph dimensions
    numPoints = graphDimensions['xmax'] - graphDimensions['xmin'] + 1
    # Create an array of x values that start at origin and end at wall
    x = np.linspace(0, distance, numPoints)
    # Calculate the initial velocity so that max hieght is maxHeight
    initialVelocity = np.sqrt((maxHeight * gravity) / np.sin(2 * np.deg2rad(launchAngle)))
    # Calculate the y values for each x value
    y = x * np.tan(np.deg2rad(launchAngle)) - (gravity * x**2) / (2 * initialVelocity**2 * np.cos(np.deg2rad(launchAngle))**2)
    
    
    return x, y



# Create graph
def graph(graphDimensions, wallDimensions, launchAngle):
    # Set axis lines to dashed black
    plt.plot([graphDimensions['xmin'], graphDimensions['xmax']], [0, 0], 'k--')
    plt.plot([0, 0], [graphDimensions['ymin'], graphDimensions['ymax']], 'k--')
    # Plot rocket starting position
    plt.plot(0,0,'ro')
    # Plot wall
    plt.plot(wallDimensions['x'], wallDimensions['y'], color='midnightblue', linewidth=5)
    # Show grid with 0.5 spacing
    plt.xticks(range(graphDimensions['xmin'], graphDimensions['xmax']+1), fontsize=fontSize)
    plt.yticks(range(graphDimensions['ymin'], graphDimensions['ymax']+1), fontsize=fontSize)
    plt.grid(which='both', ls='--', lw=0.5, color='gray', alpha=0.5)
    # Set title
    plt.title("Projectile Game", fontsize=fontSize)
    # Show coordinates of rocket and wall
    plt.text(0.3, 0.3, f"Rocket: (0, 0)", fontsize=fontSize)
    plt.text(wallDimensions['x'][0] + 0.3, wallDimensions['y'][1] + 0.3, f"Wall: ({wallDimensions['x'][0]}, {wallDimensions['y'][1]})", fontsize=fontSize)
    
    # Plot the rocket trajectory
    x, y = trajectory(graphDimensions, wallDimensions, launchAngle)
    plt.plot(x, y, 'g--', label='Rocket Trajectory')
    # Set legend
    plt.legend(fontsize=fontSize)
    
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
    # TODO: randomize function for height and wall location
    # Create graph
    graph(graphDimensions, wallDimensions, launchAngle)
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
