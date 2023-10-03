## GET CSV FILE
# via upload
# via url userinput
# via url in code

## PANDAS LIBRARY TO SAVE CSV AS A DATAFRAME

## PRINT HEADINGS AND FIRST TWO ROWS
def print_headings():
    # Get the headings
    headings = list(file.columns)
    # Get the first two rows
    firstTwoRows = file.head(2)
    #TODO 
    return print("good1")
## STORE COLUMN NAMES AS LIST

## CHOOSE 1-2 COLUMNS AND CONVERT TO NUMPY ARRAY

## DISPLAY DATA AS SCATTER PLOT/LINE GRAPH

## DYNAMIC: DIFFERENT COLUMN COMBINATIONS AND INTERPRET GRAPHS

# LIBRARIES
import pandas as pd


# * HELPER FUNCTIONS
# GET CVS FILE
def get_file():
    fileOptions = ['upload', 'url', 'demo']
    # Ask user how they want to get the file
    while True:
        print("How would you like to get the file?")
        for i, option in enumerate(fileOptions):
            print(f"{i+1}. {option}")
        userChoice = input("\nSelect an option (only enter the number): ")
        # Validate user's choice
        if userChoice.isnumeric() and int(userChoice) in range(1, len(fileOptions)+1):
            userChoice = int(userChoice)
            break
        print(f"\n {userChoice} is not a valid option. Please try again.") # print error message if invalid and try again
    # Get the file
    if userChoice == 1: # upload
        # Ask user for file
        #TODO Last in colab
        ...
    elif userChoice == 2: # url
        # Ask user for url
        url = input("Enter the url: ")
    elif userChoice == 3: # default
        # From link
        url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    return pd.read_csv(url) # return the file


# * FUNCTIONS
# INITIALIZE VARIABLES
options = {'a': print_headings}
file = []


# MENU SELECTION
def menu():
    global options
    while True:
        # Print the options
        print("\nWhat do you want to do with the file?")
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selectedOption = input("\nOnly enter the letter: ")
        # Validate the user's choice
        if selectedOption.replace('.','').lower() in options:
            selectedOption = selectedOption.replace('.','').lower() # ! ensure option is lowercase and without a period
            return selectedOption, options[selectedOption]
        print(f"\n {selectedOption} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main():
    global file
    # Get .cvs file
    if not file: # if empty
        file = get_file() # get file
    # Menu selection
    selectedOption = menu()
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()