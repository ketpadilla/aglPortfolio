# LIBRARIES
import matplotlib.pyplot as plt
from random import randint

# INITIALIZE VARIABLES
# Initialize score and launch angle
score = 0
launchAngle = randint(0, 90)
# Initialize wall dimensions
distance = randint(5, 15)
wallDimensions = {'x': [distance, distance], 'y': [0, randint(2, 20)]}
# Initialize graph dimensions
xmin, ymin, xmax, ymax = -1, -1, wallDimensions['x'][0] + 3, wallDimensions['y'][1] + 3
# Initialize font size
fontSize = max(9, 2 * min((xmax - xmin) / distance, (ymax - ymin) / distance))


# INITIALIE GRAPH
fig, ax = plt.subplots()


# FUNCTIONS
# Create rocket trajectory
def trajectory():
    return


# Create graph
def graph(xmin, ymin, xmax, ymax, wallDimensions, launchAngle):
    # Set axis lines to dashed black
    plt.plot([xmin, xmax], [0, 0], 'k--')
    plt.plot([0, 0], [ymin, ymax], 'k--')
    # Plot rocket starting position
    plt.plot(0,0,'ro')
    # Plot wall
    plt.plot(wallDimensions['x'], wallDimensions['y'], color='midnightblue', linewidth=5)
    # Show grid with 0.5 spacing
    plt.xticks(range(xmin, xmax+1), fontsize=fontSize)
    plt.yticks(range(ymin, ymax+1), fontsize=fontSize)
    plt.grid(which='both', ls='--', lw=0.5, color='gray', alpha=0.5)
    # Set title
    plt.title("Projectile Game", fontsize=fontSize)
    # Show coordinates of rocket and wall
    plt.text(0.3, 0.3, f"Rocket: (0, 0)", fontsize=fontSize)
    plt.text(wallDimensions['x'][0] + 0.3, wallDimensions['y'][1] + 0.3, f"Wall: ({wallDimensions['x'][0]}, {wallDimensions['y'][1]})", fontsize=fontSize)
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
    graph(xmin, ymin, xmax, ymax, wallDimensions, launchAngle)
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()
