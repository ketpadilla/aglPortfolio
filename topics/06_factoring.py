## FACTORING - finding the factors of a number

# --- #

# * Modulus Operator - % - returns the remainder of a division
# EXAMPLE
print("31 % 10 =", 31 % 10)

# Using modulus operator in a loop to find factors
# Initize variables
num = 12
# Loop through numbers 1 to num
for i in range(1, num + 1):
    # Check if num is divisible by i
    if num % i == 0:
        # Print factor
        print(i)

# --- #

# * Greatest Common Factor - GCF - the largest factor that two or more numbers have in common
# Initize variables
numerator = 12
denominator = 16
factor = 1
# Find GCF
for i in range(1, denominator + 1):
    if numerator%i == 0 and denominator%i == 0:
        factor = i
# Divide numerator and denominator by GCF
n = numerator / factor
d = denominator / factor
# Print original and simplified fractions
print("Original fraction:", numerator, "/", denominator)
print("Simplified fraction:", int(n), "/", int(d))

# --- #

# * Square Roots - a value that, when multiplied by itself, gives the number
# EXAMPLE:
from math import sqrt
print("sqrt(25) =", sqrt(25))

# --- #

# * Square Root Factors - the factors that are the same when a number is square rooted
# EXAMPLE: (better syntax from provided collab)
# Import sympy
from sympy import sqrt, pprint
# Input number
number = 12
# Output variable with default value
result = 1  # Default value for result
# Loop to find the maximum square factor
for i in range(1, int(sqrt(number)) + 1):
    if number % (i ** 2) == 0:
        # Update the result if a suitable factor is found
        result = int(sqrt(i ** 2)) * sqrt(number // (i ** 2))
# Print the result
pprint(result, use_unicode=False)

# --- #