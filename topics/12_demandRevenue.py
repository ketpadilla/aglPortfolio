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
# Characteristics:
# Supply curve: positive slope
# Demand curve: negative slope
# Supply and demand cuvers intersect at the equilibrium point
# Supply and demand curves will not always be linear

# --- #