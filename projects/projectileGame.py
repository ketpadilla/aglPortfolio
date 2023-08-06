# LIBRARIES
import matplotlib.pyplot as plt
from random import randint
import numpy as np


# INITIALIZE VARIABLES
# Initialize score and launch angle
score = {'correct': 0, 'total': 0}
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
    gravity = 9.81
    maxHeight, distance = wallDimensions['y'][1] + 1, wallDimensions['x'][0]
    # Calculate angle of launch and initial velocity so that the rocket hits reaches maximum height at the top of the wall
    launchAngle = round(np.arctan((2 * maxHeight) / distance),2)
    initialVelocity = round(np.sqrt((gravity * distance**2) / (2 * np.cos(launchAngle)**2 * (distance * np.tan(launchAngle) - maxHeight))),2)
    # Calculate maximum height of rocket
    maxHeight = round((initialVelocity**2 * np.sin(launchAngle)**2) / (2 * gravity),2)
    # Calculate time of flight
    flightTime = round((2 * initialVelocity * np.sin(launchAngle)) / gravity,2)
    # Calculate x and y coordinates of rocket
    pathX = np.linspace(0, distance, 100)
    pathY = (pathX * np.tan(launchAngle)) - ((gravity * pathX**2) / (2 * initialVelocity**2 * np.cos(launchAngle)**2))
    # Return path coordinates, launch angle (in degrees), initial velocity, and flight time
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
    # Turn on interactive mode
    plt.ion()
    # Display the graph
    plt.show()
    return launchAngle, initialVelocity, flightTime



# Check answer
def check(initialVelocity, answer, score):
    # Check if answer is within 0.03 of the initial velocity
    if abs(float(answer) - initialVelocity) <= 0.03:
        print("Correct!")
        score['correct'] += 1
    else:
        print("Incorrect!")
        print("The correct answer is", initialVelocity)
    score['total'] += 1
    return score

# Play again by reinitializing variables
def again(distance, wallDimensions, graphDimensions, fontSize):
    # Initialize wall dimensions
    distance = randint(5, 15)
    wallDimensions = {'x': [distance, distance], 'y': [0, randint(5, 20)]}
    # Initialize graph dimensions
    graphDimensions = {'xmin': -1, 'ymin': -1, 'xmax': wallDimensions['x'][0] + 3, 'ymax': wallDimensions['y'][1] + 3}
    # Initialize font size
    fontSize = max(9, 2 * min((graphDimensions['xmax'] - graphDimensions['xmin']) / distance, (graphDimensions['ymax'] - graphDimensions['ymin']) / distance))
    return distance, wallDimensions, graphDimensions, fontSize


# * MAIN FUNCTION
def main(maxHeight, distance, wallDimensions, graphDimensions, fontSize, score):
    # Create graph
    launchAngle, initialVelocity, flightTime = graph(graphDimensions, wallDimensions)
    # Prompt user question
    print(f"The rocket is launched at the origin (0, 0) with a launch angle of {launchAngle} radians. The rocket reaches a maximum height of {maxHeight} m, passing the wall that has a height of {maxHeight - 1} m. The rocket is in the air for {flightTime} s.")
    answer = input("What initial velocity (m/s) should the rocket be launched to satisfy these conditions? Only input the number at two decimal places: ")
    # Check answer
    score = check(initialVelocity, answer, score)
    # Ask user if they want to play again
    playAgain = input(f"Your current score is {score['correct']}/{score['total']}. Would you like to play again? (y/n): ")
    if playAgain == 'y':
        distance, wallDimensions, graphDimensions, fontSize = again(distance, wallDimensions, graphDimensions, fontSize)
        score = main(wallDimensions['y'][1] + 1, distance, wallDimensions, graphDimensions, fontSize, score)
    else:
        print("Thanks for playing!")
        score = {'correct': 0, 'total': 0}
    return score


# * RUN PROGRAM
if __name__ == "__main__":
    score = main(wallDimensions['y'][1] + 1, distance, wallDimensions, graphDimensions, fontSize, score)
    