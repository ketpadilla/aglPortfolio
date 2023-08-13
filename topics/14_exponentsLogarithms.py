## EXPONENTS AND LOGARITHMS

# --- #

# * IMPORTS
from math import e, log

# --- #

# * USAGE
# LOG: log(x, base)
logarithm = log(100, 10) # 2.0
# NATURAL LOG: e and log(x)
naturalLog = log(e) # 1.0

# --- #

# * APPLICATION
# CONTINUOUS COMPOUNDING
# Formula
rate = 0.05
time = log(2)/rate # 2 indicates doubling of investment

# ! CAN BE USED IN A GRAPH

# --- #

# * EXPONENTS
# SCIENCTIFIC NOTATION
scientificNotation1 = 1*10**3 # 1000 or 1e3
scientificNotation2 = round(1*10**-3,4) # 0.001 or 1e-3
# ! Python weirdly evaluates numbers with negative exponents, thus requiring rounding 

# --- #
