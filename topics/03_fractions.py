## FRACTIONS - numbers that expresses parts of a whole or a group.

# --- #

# * INITIALIZING EXPONENTS
exponent1 = 10 ** 3
exponent2 = 10 ** -3
print(f"Exponent 1: {exponent1}")
print(f"Exponent 2: {exponent2}")

# --- #

# * PRINTING THE LENGHT OF A STRING
# Can determine the length of number after the decimal point.
# Initizalize a number.
number = '1.23456789' # ! Already converted to string for simplicity.
# Get the lenght of the number after the decimal point.
length = len(number[number.index('.')+1:])
# Print the length of the number after the decimal point.
print(f"Number: {number} -> Length: {length}")

# --- #

# * CASTING A STRING TO A FLOAT
# Initialize a string.
string = '1.23456789'
# Cast the string to a float.
floatNumber = float(string) # ! float allows for decimal points.
# Print the float number.
print(f"String: {string} -> Float: {floatNumber}")

# --- #

# * USING COMPONENTS ABOVE TO CONVERT DECOMALS TO FRACTIONS AND PERCENTAGES
# Initialize a string.
string = '1.2'
# Cast the string to a float.
floatNumber = float(string)
# Get the length of the number after the decimal point.
length = len(string[string.index('.')+1:])
# Initialize the denominator.
denominator = 10 ** length
# Initialize the numerator.
numerator = floatNumber * denominator
# Get the percentage. Round to two decimal places.
percentage = round(floatNumber * 100, 2)
# Print the decimal.
print(f"String: {string} -> Decimal: {floatNumber}")
# Print the fraction.
print(f"String: {string} -> Fraction: {int(numerator)}/{denominator}")
# Print the percentage.
print(f"String: {string} -> Percentage: {percentage}%")

# --- #