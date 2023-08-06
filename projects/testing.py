# LIBRARIES
import matplotlib.pyplot as plt
from random import randint
import numpy as np

# INITIALIZE VARIABLES
# Initialize score and launch angle
score = 0
# Initialize wall dimensions
distance = randint(5, 15)
wallDimensions = {'x': [distance, distance], 'y': [0, randint(5, 20)]}
# Initialize graph dimensions
graphDimensions = {'xmin': -1, 'ymin': -1, 'xmax': wallDimensions['x'][0] + 3, 'ymax': wallDimensions['y'][1] + 3}
# Initialize font size
fontSize = max(9, 2 * min((graphDimensions['xmax'] - graphDimensions['xmin']) / distance, (graphDimensions['ymax'] - graphDimensions['ymin']) / distance))


# INITIALIE GRAPH
fig, ax = plt.subplots()


# FUNCTIONS
def trajectory(wallDimensions):
    # Initialize variables
    gravity = 9.8
    maxHeight, distance = wallDimensions['y'][1] + 1, wallDimensions['x'][0]
    # Calculate angle of launch and initial velocity so that the rocket hits reaches maximum height at the top of the wall
    launchAngle = np.arctan((2 * maxHeight) / distance)
    initialVelocity = np.sqrt((gravity * distance**2) / (2 * np.cos(launchAngle)**2 * (distance * np.tan(launchAngle) - maxHeight)))
    # Calculate maximum height of rocket
    maxHeight = (initialVelocity**2 * np.sin(launchAngle)**2) / (2 * gravity)
    # Calculate time of flight
    flightTime = (2 * initialVelocity * np.sin(launchAngle)) / gravity
    # Calculate x and y coordinates of rocket
    pathX = np.linspace(0, distance, 100)
    pathY = (pathX * np.tan(launchAngle)) - ((gravity * pathX**2) / (2 * initialVelocity**2 * np.cos(launchAngle)**2))
    # Return path coordinates, launch angle, initial velocity, and flight time
    return pathX, pathY, launchAngle, initialVelocity, flightTime


# Create graph
def graph(graphDimensions, wallDimensions):
    # ! SET INITIAL GRAPH DESIGN
    # Set axis lines to dashed black
    plt.plot([graphDimensions['xmin'], graphDimensions['xmax']], [0, 0], 'k--')
    plt.plot([0, 0], [graphDimensions['ymin'], graphDimensions['ymax']], 'k--')
    # Show grid with 0.5 spacing
    plt.xticks(range(graphDimensions['xmin'], graphDimensions['xmax']+1), fontsize=fontSize)
    plt.yticks(range(graphDimensions['ymin'], graphDimensions['ymax']+1), fontsize=fontSize)
    plt.grid(which='both', ls='--', lw=0.5, color='gray', alpha=0.5)
    # Set title
    plt.title("Projectile Game", fontsize=fontSize)
    # ! PLOT ROCKET TRAJECTORY 
    # Plot the rocket trajectory
    pathX, pathY, launchAngle, initialVelocity, flightTime = trajectory(wallDimensions)
    plt.plot(pathX, pathY, 'g--', alpha=0.5, label='Expected Rocket Trajectory')
    # Add an arrow at the end of the line
    plt.annotate('', xy=(pathX[-1], pathY[-1]), xytext=(pathX[-2], pathY[-2]),arrowprops=dict(arrowstyle='->', color='g', alpha=0.5))
    # ! PLOT ROCKET
    # Plot rocket starting position
    plt.plot(0,0,'ro')
    # Show coordinates of rocket
    plt.text(0.3, 0.3, f"Rocket: (0, 0)", fontsize=fontSize)
    # ! PLOT WALL
    # Plot wall
    plt.plot(wallDimensions['x'], wallDimensions['y'], color='midnightblue', linewidth=5)
    # Show coordinates of wall
    plt.text(wallDimensions['x'][0] + 0.3, wallDimensions['y'][1] + 0.3, f"Wall: ({wallDimensions['x'][0]}, {wallDimensions['y'][1]})", fontsize=fontSize)
    # ! SET FINAL GRAPH DESIGN
    # Set legend
    plt.legend(fontsize=fontSize)
    # Show graph
    plt.show()
    return launchAngle, initialVelocity, flightTime



# Check if ... 
def check():
    # TODO: for initial velocity
    ...
    return score


# TODO: graph animation


# * MAIN FUNCTION
def main():
    # Create graph
    launchAngle, initialVelocity, flightTime = graph(graphDimensions, wallDimensions)
    # Print launch angle and initial velocity
    print(f"Launch angle: {launchAngle}")
    print(f"Initial velocity: {initialVelocity}")
    print(f"Flight time: {flightTime}")
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
