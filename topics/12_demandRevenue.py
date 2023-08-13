## CALCULATING DEMAND AND 

# --- #

# * VARIABLES
from sympy import symbols
a, b = symbols('a b')
price = a
demand = b - 2*price

# --- #

# * EQUATIONS
revenue = price * demand
totalCost = 4*demand
profit = revenue - totalCost

# ! NOTE: variables can be used in graphs

# --- #