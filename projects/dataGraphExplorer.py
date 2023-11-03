# LIBRARIES
import pandas as pd

# * HELPER FUNCTIONS
# SET CSV TO DATAFRAME
def get_df():
    # Get file option
    fileOpt, source = get_file()
    if fileOpt == 'demo':
        source = 'docs/addresses.csv'
    return pd.read_csv(source) ##! CSV saved as a pandas dataframe


# GET FILE
def get_file():
    #! TODO
    return 'demo', ''


# CONVERT TO NUMPY ARRAY
def to_numpy():
    return df.to_numpy()


# * FUNCTIONS
# PRINT HEADINGS
def print_headings():
    return [print(heading) for heading in df.columns]


# PRINT FIRST TWO ROWS
def print_first_two_rows():
    return print(df.head(2))


# SHOW SCATTER PLOT
def show_scatter_plot(): 
    # Convert column names to list
    columns = df.columns.tolist() ##! Column names converted to list
    print(columns)
    return


# * GLOBAL VARIABLES
options = {'a': print_headings, 'b': print_first_two_rows, 'c': show_scatter_plot}
df = []

# MENU SELECTION
def menu():
    global options
    while True:
        # Print options
        for key, value in options.items():
            print(f"{key}. {value.__name__.replace('_',' ')}")
        # Get the user's choice
        selected = input("\nSelect an option (only enter the letter): ")
        # Validate the user's choice
        if selected.replace('.','').lower() in options:
            selected = selected.replace('.','').lower() # ! ensure option is lowercase and without a period
            # Run the selected option
            return options[selected]()
        print(f"\n {selected} is not a valid option. Please try again.") # print error message if invalid and try again


# * MAIN FUNCTION
def main():
    global df
    if not df: # if empty
        df = get_df() # get csv
    return menu() # run menu


# * RUN PROGRAM
if __name__ == "__main__":
    main()