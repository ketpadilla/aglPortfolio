## ACCESSING AND USING SPREADSHEETS

# --- #

# * PANDAS

import pandas as pd # ! pip install pandas
# from google.colab import files # ! for uploading files to colab

# * GETTING CSV FILES 
# From link
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# Read csv file
data = pd.read_csv(url)
# Get headers
columns = data.columns
# Converting to numpy array
data = data.to_numpy() # ! use variableName[columns[#]].to_numpy() to convert a column to numpy array

# --- #

# ! USED FOR APPLICATIONS LIKE GRAPHING WEAHTER DATA
# ! COLAB CODE SNIPPETS ARE AVAIALBLE IN THE COLAB NOTEBOOK