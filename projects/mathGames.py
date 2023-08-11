# LIBRARIES
import matplotlib.pyplot as plt
from random import randint
from numpy import linspace, sqrt, sin, cos, tan, arctan
from inspect import stack


# * HELPER FUNCTIONS
# ASK FOR THE NUMBER OF QUESTIONS
def ask_rounds():
    while True:
        try:
            rounds = int(input("\nHow many rounds would you like to play? "))
            if rounds < 1:
                print("Please enter a positive integer.")
                continue
            return rounds
        except ValueError:
            print("Please enter a positive integer.")
            continue


# SET FONT SIZE
def set_fontsize(graphDimensions):
    return max(9, (graphDimensions['xmax'] - graphDimensions['xmin']) / 2)


# CREATE GRAPH
def graph(round, graphDimensions, fontSize):
    # ! PRINT ROUND
    print(f"\nRound {round+1}")
    # ! SET GRAPH DESIGN
    # Initialize graph
    fig, ax = plt.subplots()
    # Set axis lines to dashed black
    plt.plot([graphDimensions['xmin'], graphDimensions['xmax']], [0, 0], 'k--')
    plt.plot([0, 0], [graphDimensions['ymin'], graphDimensions['ymax']], 'k--')
    # Show grid with 0.5 spacing
    plt.xticks(range(graphDimensions['xmin'], graphDimensions['xmax']+1), fontsize=fontSize-10)
    plt.yticks(range(graphDimensions['ymin'], graphDimensions['ymax']+1), fontsize=fontSize-10)
    plt.grid(which='both', ls='--', lw=0.5, color='gray', alpha=0.5)
    # Set title
    plt.title(f"{options[selectedOption[0]].__name__.replace('_',' ').title()}", fontsize=fontSize)
    # Determine if function is being called from scatter_plot or projectiles
    # ! SCATTER PLOT
    if stack()[1][3] == 'scatter_plot':
        # Create a random point
        x, y = randint(graphDimensions['xmin'], graphDimensions['xmax']), randint(graphDimensions['ymin'], graphDimensions['ymax'])
        # Plot the point
        plt.plot(x, y, 'o')
        # Store point in answer
        answer = [x, y]
        # Show graph
        show_graph(True)
        return answer
    # ! PROJECTILES
    # TODO
    print("projectiles")
    return answer


# SHOW AND CLOSE GRAPH
def show_graph(showStatus):
    if showStatus == False:
        # Prompt input if function is not being called from check_scatter
        if stack()[1][3] != 'check_scatter':
            input("Press enter to close the graph.")
        plt.close()
        return plt.ioff()
    plt.ion()
    return plt.show()


# VALIDATE GUESS 1
def guess_empty(guess, function):
    # Check if function was called from check_scatter
    if function == 'check_scatter':
        # Check if guess is empty or incomplete
        if guess == '' or guess.count(',') != 1:
            print("Input is empty or incomplete.")
            return True
    # Check if guess is only empty
    if guess == '':
        print("Input is empty.")
        return True
    return False


# VALIDATE GUESS 2
def guess_integer(guess, function):
    # Check if function was called from check_scatter
    if function == 'check_scatter':
        # Separate user input into x and y coordinates
        guess = guess.split(',')
        x, y = guess[0].strip().replace('(',''), guess[1].strip().replace(')','')
        # Remove "-" sign then check if the input can be converted to an integer
        if x.replace('-','').isdigit() == False or y.replace('-','').isdigit() == False:
            print("Either x or y is not an integer.")
            return True
        return False
    # Assume guess is only one number
    # Remove "-" sign then check if the input can be converted to an integer
    if guess.replace('-','').isdigit() == False:
        print("Input is not an integer.")
        return True
    return False


# VALIDATE GUESS 3
def guess_validate(guess):
    # Check if both validations are false
    if guess_empty(guess, stack()[1][3]):
        return True
    if guess_integer(guess, stack()[1][3]):
        return True
    # Else, proceed
    return False


# CHECK SCATTER PLOT ANSWER
def check_scatter(guess, answer, score):
    # Increment total score
    score['total'] += 1
    # Check if guess is valid
    if guess_validate(guess):
        # Print correct answer if guess is invalid
        print(f"The correct answer was ({answer[0]},{answer[1]}).")
        return score
    # Separate user input into x and y coordinates
    guess = guess.split(',')
    x, y = guess[0].strip().replace('(',''), guess[1].strip().replace(')','')
    # Check if the answer is correct
    if int(x) == int(answer[0]) and int(y) == int(answer[1]):
        print("Correct!")
        score['correct'] += 1
        return score
    # Print correct answer
    print(f"Sorry, the correct answer was ({answer[0]},{answer[1]}).")
    return score


# RETURN FINAL SCORE
def return_score(score):
    # Print final score
    print(f"\nScore: {score['correct']}/{score['total']}")
    # Return score
    return score


# GENERATE ADDITION QUESTION
def add():
    # Increment total score
    score['total'] += 1
    # Generate random numbers
    a, b = randint(-50, 100), randint(-50, 100)
    # Store answer
    answer = b - a
    # Print question
    print(f"\nSolve for x:\nx + {a} = {b}")
    # Get user input
    guess = input("x = ")
    # Check if guess is valid
    if guess_validate(guess):
        # Print correct answer if guess is invalid
        print(f"The correct answer was {answer}.")
        return score
    # Check if the answer is correct
    if int(guess) == answer:
        print("Correct!")
        score['correct'] += 1
        return score
    return score


# * FUNCTIONS
# SCATTER PLOT GAME
def scatter_plot():
    global score
    # Ask for the number of rounds
    rounds = ask_rounds()
    # Initialize variables
    graphDimensions = {'xmin': -15, 'ymin': -15, 'xmax': 15, 'ymax': 15}
    fontSize = set_fontsize(graphDimensions)
    # Start game
    for i in range(0, rounds):
        # Create graph
        answer = graph(i, graphDimensions, fontSize)
        # Ask for the coordinates
        guess = input("Enter the coordinates of the point (x,y): ")
        # Validate the answer
        score = check_scatter(guess, answer, score)
        # Close graph
        plt.close()
    return return_score(score)


# ALGEBRA PRACTICE GAME
def algebra_practice():
    # Ask for the number of rounds
    rounds = ask_rounds()
    # Start game
    for i in range(0, rounds):
        score = add()
        score = subtract()
        score = multiply()
        score = divide()
        score = x()
    return return_score(score)


# PROJECTILE GAME
def projectiles():
    # Ask for the number of rounds
    rounds = ask_rounds()
    # Initialize variables

    # Start game
    # TODO

    return return_score(score)


# INITIALIZE VARIABLES
options = {'a': scatter_plot, 'b': algebra_practice, 'c': projectiles}
score = {'correct': 0, 'total': 0}


# MENU SELECTION
def menu(options):
    while True:
        # Print the options
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selectedOption = input("\nSelect a game to play (only enter the letter): ")
        # Validate the user's choice
        if selectedOption.replace('.','').lower() in options:
            selectedOption = selectedOption.replace('.','').lower() # ! ensure option is lowercase and without a period
            return selectedOption, options[selectedOption]
        print(f"\n {selectedOption} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main(options):
    global score, selectedOption
    # Menu selection
    selectedOption = menu(options)
    # Call the function based on the user's choice
    score = options.get(selectedOption[0], lambda: print("Error: Invalid option."))()
    # TODO: Prompt user to play again
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main(options)
    