## SIMPLE AND COMPOUND INTEREST

# --- #

# * SIMPLE INTEREST
# Formula
principle, rate, time = 1000, 0.05, 5
interest = principle * rate * time
# Outstanding amount
amount = principle + interest

# --- #

# * COMPOUND INTEREST
# General Formula
interest = principle * (1 + rate)**time
# Outstanding amount
amount = principle + interest
# Formula for "n" compounding periods per year
n = 1 # yearly; 2 for semi-annually; 4 for quarterly; 12 for monthly
annuity = principle * (1 + rate/n)**(n*time)

# --- #

# * CONTINUOUS COMPOUNDING
# Formula
from math import e
annuity = principle * e**(rate*time)

# --- #

# * MORTGAGE
# Formula
monthlyPayment = principle * (rate/(1 - (1 + rate)**(-time)))
# Amortization
# ! REFER TO FILE: https://colab.research.google.com/drive/1IVBaeX84arJXS73raRROaxbz4qMyFVb6?usp=sharing

# --- #

# ! EXTRA: plotting principle vs. payment