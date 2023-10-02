## GET CSV FILE
# via upload
# via url userinput
# via url in code

## PANDAS LIBRARY TO SAVE CSV AS A DATAFRAME

## PRINT HEADINGS AND FIRST TWO ROWS
def print_headings():
    return print("good1")
## STORE COLUMN NAMES AS LIST

## CHOOSE 1-2 COLUMNS AND CONVERT TO NUMPY ARRAY

## DISPLAY DATA AS SCATTER PLOT/LINE GRAPH

## DYNAMIC: DIFFERENT COLUMN COMBINATIONS AND INTERPRET GRAPHS

# LIBRARIES


# * HELPER FUNCTIONS
# GET CVS FILE
def get_file():
    return file


# * FUNCTIONS
# INITIALIZE VARIABLES
options = {'a': print_headings}
file = None


# MENU SELECTION
def menu():
    global options, graphDimensions, fontSize
    while True:
        # Print the options
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selectedOption = input("\nSelect an option (only enter the letter): ")
        # Validate the user's choice
        if selectedOption.replace('.','').lower() in options:
            selectedOption = selectedOption.replace('.','').lower() # ! ensure option is lowercase and without a period
            return selectedOption, options[selectedOption]
        print(f"\n {selectedOption} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main():
    # Get .cvs file
    if not file: # if empty
        file = get_file() # get file
    # Menu selection
    selectedOption = menu()
    return


# * RUN PROGRAM
if __name__ == "__main__":
    main()