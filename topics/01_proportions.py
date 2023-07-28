## PROPORTIONS - an equation where two ratios (e.g., a/b) are set equal to each other

# --- #

# ! Using fractions as is (e.g., print(a/b)) will NOT work. Its numerator and denaminator must in initialized and placed into separate variables. 

# * CONVERTING STRING TO FRACTION
def string2Fraction():
    string = input("Input number: ")
    # Determine if input is a fraction
    if "/" in string:
        # Split the input into numerator and denominator (e.g., "a/b" -> ["a", "b"])
        numerator, denominator = string.split("/")
        # Cast string to int
        # ! Use float if you want to allow decimals
        numerator, denominator = int(numerator), int(denominator)
        # Return the fraction
        return f"Numerator = {numerator}, Denominator = {denominator}"
    # If input is not a fraction, return the input as an int
    return f"{string} is not a fraction"

# Call function
print(string2Fraction())

# --- #

from random import randint, random

# * CONVERTING DECIMAL TO FRACTION
def decimal2Fraction():
    # Generate a random decimal
    places = randint(1,4)
    decimal = round(random(), places)
    # Convert decimal to fraction
    denaminator = 10 ** places
    numerator = int(decimal * denaminator)
    # Return decimal and fraction
    return f"{decimal}" + " -> " + f"{numerator} / {denaminator}"

# Call function
print(decimal2Fraction())

# --- #

# * CONVERTING FRACTION TO PERCENT
def fraction2Percent():
    # Generate a random fraction
    numerator, denaminator = randint(1, 100), randint(1, 100)
    # Convert fraction to percent (with 2 decimal places)
    percent = round(numerator / denaminator * 100, 2)
    return f"{numerator} / {denaminator} = {percent}%"

# Call function
print(fraction2Percent())

# --- #