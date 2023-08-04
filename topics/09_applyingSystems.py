# APPLICATINOS OF SYSTEMS OF EQUATIONS
# ! Problems provided by the book may be outside the source of the provided topic (or maybe I mistakingly missed the correct pages)

# --- #

# IMPORTS
from sympy import symbols, pretty, solve, simplify, Eq, sqrt, sympify
from numpy import log

# * PROBLEM 1
eq = (1+(0.0725/12)**(2/4))-1
# Print the answer
print(f"\nProblem 1: (1+(0.0725/12)^(2/4))-1 = {round(eq,2)}")

# * PROBLEM 2
# Convert 4(12/37) to a decimal
eq = 4*(12/37)
# Print the answer
print(f"\nProblem 2: 4(12/37) = {round(eq,2)}")

# * PROBLEM 3
# Get percentage of 321/450
eq = (321/450)*100
# Print the answer
print(f"\nProblem 3: (321/450)*100 = {round(eq,2)}%")

# * PROBLEM 4
# Simplify 16x^2/4x - 21x^3y^2/7x^2y^2
x, y = symbols('x y')
eq = 16*x**2/(4*x) - 21*x**3*y**2/(7*x**2*y**2)
# Simplify the equation
eq = simplify(eq)
# Print the answer
print(f"\nProblem 4: 16x^2/4x - 21x^3y^2/7x^2y^2 = {pretty(eq)}")

# * PROBLEM 5
# Solve for r: -2r - 2.25 = 3.75 - 8r
r = symbols('r')
eq = -2*r - 2.25 - (3.75 - 8*r)
# Solve for r
eq = solve(eq, r)
# Print the answer
print(f"\nProblem 5: r in (-2r - 2.25 = 3.75 - 8r) = {eq[0]}")

# * PROBLEM 6 
# Demonstrat 3*ln(2) = ln(2^3)
eq = 3*log(2) - log(2**3)
# Print the answer
print(f"\nProblem 6: 3*ln(2) - ln(2^3) = {eq}. Therefore, 3*ln(2) = ln(2^3)")

# * PROBLEM 7
a = 0.14/4
b = 0.06
c = 1725
d = 7
eq = b * c * ((1-(1+a)**(-d))/a)
# Print the answer
print(f"\nProblem 7: {round(eq,2)}")

# * PROBLEM 8
a = 0.0975/4
b = 3225
c = 255
eq = (1+((a*b)/c))/(1+a)
# Print the answer
print(f"\nProblem 8: {round(eq,2)}")

# * PROBLEM 9
# 15% of a 240 ml bottle is real fruit juice. How many ml of other ingredients are in the bottle?
a = 0.15
b = 240
eq = b - (a*b)
# Print the answer
print(f"\nProblem 9: {round(eq,2)}")

# * PROBLEM 10
# Full-time employees work for 39.5 hours per week. An adult required 8 hours of sleep per day. What percentage of hours is left for other activities?
a = 39.5
b = 7*8
eq = ((a-b)/a)*100
# Print the answer
print(f"\nProblem 10: {round(eq,2)}%")

# * PROBLEM 11
a = 535
b = 0.025
c = 6
eq = a*(((1+b)**c-1)/b)
# Print the answer
print(f"\nProblem 11: a(((1+b)^c-1)/b) = {round(eq,2)}")

# * PROBLEM 12
# Simplify: (15a^7b^3c^2/5a^5c)^3 / (9a^4b^6c^5/3a^2b^2c^3)^(3/2)
a, b, c = symbols('a b c')
eq = ((15*a**7*b**3*c**2)/(5*a**5*c))**3 / ((9*a**4*b**6*c**5)/(3*a**2*b**2*c**3))**(3/2)
# Simplify the equation
eq = simplify(eq)
# Print the answer
print(f"\nProblem 12:\n{pretty(eq)}")

# * PROBLEM 13
# Simplify: PMT(1-(1+0.0225)^6(1+0.044)^(-6)/(0.044-0.0225)) + PMT((1/0.044)+1)
PMT = symbols('PMT')
eq = PMT*(1-(1+0.0225)**6*(1+0.044)**(-6)/(0.044-0.0225)) + PMT*((1/0.044)+1)
# Simplify the equation
eq = simplify(eq)
# Print the answer
print(f"\nProblem 13:\n{pretty(eq)}")

# * PROBLEM 14
# Housing starts in Winnipeg for the first half of the 2009 year were down 46.733% from 2008, when 1,500 new homes were started. How many housing starts were there in 2009?
a = 0.46733
b = 1500
eq = b*(1-a)
# Print the answer
print(f"\nProblem 14: {round(eq,2)}")

# * PROBLEM 15
# A local baseball team sells tickets with two price zones. Seats behind the plate from first base to third base are priced at $20 per ticket. All other seats down the base lines and in the outfield are priced at $10 per ticket. At last night's game, 5,332 fans were in attendance and total ticket revenue was $71,750. How many tickets in each zone were sold?
a = 20
b = 10
eq1 = (a*x) + (b*y)
eq2 = x + y
c = Eq(eq1, 71750)
d = Eq(eq2, 5332)
# Solve for x and y
eq = solve((c,d), (x,y))
# Print the answer
print(f"\nProblem 15: Tickets sold in each zone: {round(eq[x],2)} and {round(eq[y],2)}")

# * PROBLEM 16
# Percent Change: Old = 109.95, New = 115.45
a = 109.95
b = 115.45
eq = ((b-a)/a)*100
# Print the answer
print(f"\nProblem 16: {round(eq,2)}%")

# * PROBLEM 17
# Old Price: New = 622.03, Percent Change = 13.25%
a = 622.03
b = 13.25
eq = a/(1+(b/100))
# Print the answer
print(f"\nProblem 17: {round(eq,2)}") 

# * PROBLEM 18
# New Price: Old = 5.84%, Percent Change = -10%
a = 5.84
b = -10
eq = a*(1+(b/100))
# Print the answer
print(f"\nProblem 18: {round(eq,2)}")

# * PROBLEM 19
# If $9.99 is changed to $10.49, what is the percent change?
a = 9.99
b = 10.49
eq = ((b-a)/a)*100
# Print the answer
print(f"\nProblem 19: {round(eq,2)}%")

# * PROBLEM 20
# $19.99 lowered by 10% is what dollar amount?
a = 19.99
b = 10
eq = a*(1-(b/100))
# Print the answer
print(f"\nProblem 20: {round(eq,2)}")

# * PROBLEM 21
# What amount when increased by 40% is $3,500?
a = 3500
b = 40
eq = a/(1+(b/100))
# Print the answer
print(f"\nProblem 21: {round(eq,2)}")

# * PROBLEM 22
# If 10,000 grows to 20,000 over a period of 10 years, what is the annual rate of change?
a = 10000
b = 20000
c = 10
eq = ((b/a)**(1/c)-1)*100
# Print the answer
print(f"\nProblem 22: {round(eq,2)}%")

# * PROBLEM 23
# A $1,000 investment was purchased one year ago and its value declines to $800 today. Over the holding period, $200 of income was generated. Calculate the income yield, capital gain yield, and the investment total rate of return.
a = 1000
b = 800
c = 200
eq1 = (c/a)*100
eq2 = ((b-a)/a)*100
eq3 = ((b+c-a)/a)*100
# Print the answer
print(f"\nProblem 23: Income Yield = {round(eq1,2)}%, Capital Gain Yield = {round(eq2,2)}%, Total Rate of Return = {round(eq3,2)}%")

# * PROBLEM 24
# Last year, an investor purchased some shares for $7,500. Today they are worth $11,250. Over the holding period, the shares paid dividends totaling to $150. Calculate the income yield, capital gain yield, and the investment total rate of return.
a = 7500
b = 11250
c = 150
eq1 = (c/a)*100
eq2 = ((b-a)/a)*100
eq3 = ((b+c-a)/a)*100
# Print the answer
print(f"\nProblem 24: Income Yield = {round(eq1,2)}%, Capital Gain Yield = {round(eq2,2)}%, Total Rate of Return = {round(eq3,2)}%")

# * PROBLEM 25
# How much, including taxes of 12%, would you pay for an item with a retail price of $194.95?
a = 194.95
b = 12
eq = a*(1+(b/100))
# Print the answer
print(f"\nProblem 25: {round(eq,2)}")

# * PROBLEM 26
# From September 8, 2007 to November 7, 2007, the Canadian dollar experienced a rapid appreciation against the US dollar, going from $0.9482 to $1.1024. What was the percent increase in the Canadian dollar?
a = 0.9482
b = 1.1024
eq = ((b-a)/a)*100
# Print the answer
print(f"\nProblem 26: {round(eq,2)}%")

# * PROBLEM 27
# From 1996 to 2006, the “big three” automakers in North America (General Motors, Ford, and Chrysler) saw their market share drop from 71.5% to 52.7%. What is the overall change and the rate of change per year?
a = 71.5
b = 52.7
c = 1996
d = 2006
eq1 = ((b-a)/a)*100
eq2 = ((b/a)**(1/(d-c))-1)*100
# Print the answer
print(f"\nProblem 27: Overall Change = {round(eq1,2)}%, Rate of Change Per Year = {round(eq2,2)}%")

# * PROBLEM 28
# TheaveragepriceofhomesinCalgaryfellby$10,000to$357,000fromJune2009toJuly2009.TheJune2009price was 49% higher than the June 2005 price. a. What was the percent change from June 2009 to July 2009? b. What was the average price of a home in June 2005? c. What was the annual rate of change from June 2005 to June 2009?
a = 10000
b = 357000
c = 49
d = 2005
e = 2009
eq1 = ((b-a)/b)*100
eq2 = b/(1+(c/100))
eq3 = ((b/eq2)**(1/(e-d))-1)*100
# Print the answer
print(f"\nProblem 28: Percent Change from June 2009 to July 2009 = {round(eq1,2)}%, Average Price of a Home in June 2005 = {round(eq2,2)}, Annual Rate of Change from June 2005 to June 2009 = {round(eq3,2)}%")

# * PROBLEM 29
# On October 28, 2006, Saskatchewan lowered its provincial sales tax (PST) from 7% to 5%. What percent reduction does this represent?
a = 7
b = 5
eq = ((a-b)/a)*100
# Print the answer
print(f"\nProblem 29: {round(eq,2)}%")

# * PROBLEM 30
# A local Superstore sold 21,983 cases of its President's Choice cola at $2.50 per case. In the following year, it sold 19,877 cases at $2.75 per case. 1. What is the percent change in price year-over-year? 2. What is the percent change in quantity year-over-year? 3. What is the percent change in total revenue year-over-year? (Hint: revenue = price × quantity)
a = 21983
b = 19787
c = 2.5
d = 2.75
eq1 = ((d-c)/c)*100
eq2 = ((b-a)/a)*100
eq3 = (((b*d)-(a*c))/(a*c))*100
# Print the answer
print(f"\nProblem 30: Percent Change in Price Year-Over-Year = {round(eq1,2)}%, Percent Change in Quantity Year-Over-Year = {round(eq2,2)}%, Percent Change in Total Revenue Year-Over-Year = {round(eq3,2)}%")

# * PROBLEM 31
# A bottle of liquid laundry detergent priced at $16.99 for a 52-load bottle has been changed to $16.49 for a 48-load bottle. By what percentage has the price per load changed?    
a = 16.99
b = 16.49
c = 52
d = 48
eq = (((b*d)-(a*c))/(a*c))*100
# Print the answer
print(f"\nProblem 31: {round(eq,2)}%")

# * PROBLEM 32
# Average of 8,17,6,33,15,12,13,16
data = [8,17,6,33,15,12,13,16]
eq = sum(data)/len(data)
# Print the answer
print(f"\nProblem 32: {round(eq,2)}")

# * PROBLEM 33
# Average of $1,500 $2,000 $1,750 $1,435 $2,210
data = [1500,2000,1750,1435,2210]
eq = sum(data)/len(data)
# Print the answer
print(f"\nProblem 33: {round(eq,2)}")

# * PROBLEM 34
# Weighted average of 4 4 4 4 12 12 12 12 12 12 12 15 15
data = [4,4,4,4,12,12,12,12,12,12,12,15,15]
eq = sum(data)/len(data)
# Print the answer
print(f"\nProblem 34: {round(eq,2)}")

# * PROBLEM 35
# Weighted average of DATA: $3,600 $3,300 $3,800 $2,800 $5,800; WEIGHT: 2 5 3 6 4
data = [3600,3300,3800,2800,5800]
weight = [2,5,3,6,4]
eq = sum([a*b for a,b in zip(data,weight)])/sum(weight)
# Print the answer
print(f"\nProblem 35: {round(eq,2)}")

# * PROBLEM 36
# Geometric average (in four decimals): 5.4% 8.7% 6.3%
data = [0.054,0.087,0.063]
eq = (data[0]*data[1]*data[2])**(1/3)-1
# Print the answer
print(f"\nProblem 36: {round(eq,4)}")

# * PROBLEM 37
# Geometric average (in four decimals): 10% −4% 17% −10%
data = [0.1,-0.04,0.17,-0.1]
eq = (data[0]*data[1]*data[2]*data[3])**(1/4)-1
# Print the answer
print(f"\nProblem 37: {round(eq,4)}")

# * PROBLEM 38
# If a 298 mL can of soup costs $2.39, what is the average price per millilitre?
a = 298
b = 2.39
eq = b/a
# Print the answer
print(f"\nProblem 38: {round(eq,4)}")

# * PROBLEM 39
# Kerry participated in a fundraiser for the Children's Wish Foundation yesterday. She sold 115 pins for $3 each, 214 ribbons for $4 each, 85 coffee mugs for $7 each, and 347 baseball hats for $9 each. Calculate the average amount Kerry raised per item.
a, b, c, d, eq = 115, 214, 85, 347, (a*3+b*4+c*7+d*9)/(a+b+c+d)
# Print the answer
print(f"\nProblem 39: {round(eq,2)}")

# * PROBLEM 40
# Stephanie’s mutual funds have had yearly changes of 9.63%, −2.45%, and 8.5%. Calculate the annual average change in her investment.
data = [9.63,-2.45,8.5]
eq = sum(data)/len(data)
# Print the answer
print(f"\nProblem 40: {round(eq,2)}%")

# * PROBLEM 41
# In determining the hourly wages of its employees, a company uses a weighted system that factors in local, regional, and national competitor wages. Local wages are considered most important and have been assigned a weight of 5. Regional and national wages are not as important and have been assigned weights of 3 and 2, respectively. If the hourly wages for local, regional, and national competitors are $16.35, $15.85, and $14.75, what hourly wage does the company pay?
data = [16.35,15.85,14.75]
weight = [5,3,2]
eq = sum([a*b for a,b in zip(data,weight)])/sum(weight)
# Print the answer
print(f"\nProblem 41: {round(eq,2)}")

# * PROBLEM 42
# Canadian Tire is having an end-of-season sale on barbecues, and only four floor models remain, priced at $299.97, $345.49, $188.88, and $424.97. What is the average price for the barbecues?
data = [299.97,345.49,188.88,424.97]
eq = sum(data)/len(data)
# Print the answer
print(f"\nProblem 42: {round(eq,2)}")

# * PROBLEM 43
# Calculate the grade point average (GPA) for the following student. Round your answer to two decimals.
# Course	Grade	Weight
# Economics100 D 5
# Math100 B 3
# Marketing100 C 4
# Communications100 A 2
# Computing100 A+ 3
# Accounting100 B+ 4
# Grade GradePoint
# A+ 4.5
# A 4.0
# B+ 3.5
# B 3.0
# C+ 2.5
# C 2.0
# D 1.0
# F 0.0
data, weight = [1,3,2,4,4.5,3.5], [5,3,4,2,3,4]
eq = sum([a*b for a,b in zip(data,weight)])/sum(weight)
# Print the answer
print(f"\nProblem 43: {round(eq,2)}")

# * PROBLEM 44
# Laars earns an annual salary of $60,000. Determine his gross earnings per pay period under each of the following payment frequencies: a. Monthly b. Semi-monthly c. Biweekly d. Weekly
a, b, c, d = 60000/12, 60000/24, 60000/26, 60000/52
# Print the answer
print(f"\nProblem 44: a. {round(a,2)} b. {round(b,2)} c. {round(c,2)} d. {round(d,2)}")

# * PROBLEM 45
# A worker earning $13.66 per hour works 47 hours in the first week and 42 hours in the second week. What are his total biweekly earnings if his regular workweek is 40 hours and all overtime is paid at 1.5 times his regular hourly rate?
a, b, c = 13.66, 47, 42
eq = (40*a)+(7*a*1.5)+(2*a)+(2*a*1.5)
# Print the answer
print(f"\nProblem 45: {round(eq,2)}")

# * PROBLEM 46
# Marley is an independent sales agent. He receives a straight commission of 15% on all sales from his suppliers. If Marley averages semi-monthly sales of $16,000, what are his total annual gross earnings?
a, b = 0.15, 16000
eq = (b*24)*a
# Print the answer
print(f"\nProblem 46: {round(eq,2)}")

# * PROBLEM 47
# Sheila is a life insurance agent. Her company pays her based on the annual premiums of the customers that purchase life insurance policies. In the last month, Sheila's new customers purchased policies worth $35,550 annually. If she receives 10% commission on the first $10,000 of premiums and 20% on the rest, what are her total gross earnings for the month?
a, b, c = 0.1, 0.2, 35550
eq = (10000*a)+(25550*b)
# Print the answer
print(f"\nProblem 47: {round(eq,2)}")

# * PROBLEM 48
# Tuan is a telemarketer who earns $9.00 per hour plus 3.25% on any sales above $1,000 in any given week. If Tuan works 35 regular hours and sells $5,715, what are his gross earnings for the week?
a, b, c = 9, 0.0325, 5715
eq = (35*a)+(c-1000)*b
# Print the answer
print(f"\nProblem 48: {round(eq,2)}")

# * PROBLEM 49
# Adolfo packs fruit in cans on a production line. He is paid a minimum wage of $9.10 per hour and earns $0.09 for every can packed. If Adolfo manages to average 160 cans per hour, what are his total gross earnings daily for an eight-hour shift?
a, b, c = 9.1, 0.09, 160
eq = (8*a)+(8*c*b)
# Print the answer
print(f"\nProblem 49: {round(eq,2)}")

# * PROBLEM 50
# Charles earns an annual salary of $72,100 paid biweekly based on a regular workweek of 36.25 hours. His company generously pays all overtime at twice his regular wage. If Charles worked 85.5 hours over the course of two weeks, what are his gross earnings?
a, b, c, d = 72100/26, 36.25, 85.5, 2
eq = (a*b)+(c-d*b)*d
# Print the answer
print(f"\nProblem 50: {round(eq,2)}")

# * PROBLEM 51
# Armin is the payroll administrator for his company. In looking over the payroll, he notices the following workweek (from Sunday to Saturday) for one of the company's employees: 0, 6, 8, 10, 9, 8, and 9 hours, respectively. Monday was a statutory holiday, and with business booming the employee will not be given another day off in lieu. Company policy pays all overtime at time-and-a-half, and all hours worked on a statutory holiday are paid at twice the regular rate. A normal workweek consists of five, eight-hour days. If the employee receives $22.20 per hour, what are her total weekly gross earnings?
a, b, c, d, e, f, g, h = 0, 6, 8, 10, 9, 8, 9, 22.2
eq = (5*h)+(b*h*1.5)+(c*h*1.5)+(d*h*1.5)+(e*h*1.5)+(f*h*1.5)+(g*h*2)
# Print the answer
print(f"\nProblem 51: {round(eq,2)}")

# * PROBLEM 52
# In order to motivate a manufacturer's agent to increase his sales, a manufacturer offers monthly commissions of 1.2% on the first $125,000, 1.6% on the next $150,000, 2.25% on the next $125,000, and 3.75% on anything above. If the agent managed to sell $732,000 in a single month, what commission is he owed?
a, b, c, d, e, f, g = 0.012, 0.016, 0.0225, 0.0375, 125000, 150000, 732000
eq = (a*g)+(b*g)+(c*g)+(d*(g-(e*3)))
# Print the answer
print(f"\nProblem 52: {round(eq,2)}")

# * PROBLEM 53
# Humphrey and Charlotte are both sales representatives for a pharmaceutical company. In a single month, Humphrey received $5,545 in total gross earnings while Charlotte received $6,388 in total gross earnings. In sales dollars, how much more did Charlotte sell if they both received 5% straight commission on their sales?
a, b, c = 5545, 6388, 0.05
eq = (b-a)/c
# Print the answer
print(f"\nProblem 53: {round(eq,2)}")

# * PROBLEM 54
# Mayabel is a cherry picker working in the Okanagan Valley. She can pick 17 kg of cherries every hour. The cherries are placed in pails that can hold 13.6 kg of cherries. If she works 40 hours in a single week, what are her total gross earnings if her piecework rate is $17.00 per pail?
a, b, c, d, e = 17, 13.6, 40, 17, 17*13.6
eq = (a*b)*c
# Print the answer
print(f"\nProblem 54: {round(eq,2)}")

# * PROBLEM 55
# Miranda is considering three relatively equal job offers and wants to pick the one with the highest gross earnings. The first job is offering a base salary of $1,200 semi-monthly plus 2% commission on monthly sales. The second job offer consists of a 9.75% straight commission. Her final job offer consists of monthly salary of $1,620 plus 2.25% commission on her first $10,000 in monthly sales and 6% on any monthly sales above that amount. From industry publications, she knows that a typical worker can sell $35,000 per month. Which job offer should she choose, and how much better is it than the other job offers?
a = 1200
b = 0.02
c = 0.0975
d = 1620
e = 0.0225
f = 0.06
g = 10000
h = 35000
eq1 = (a*24)+(h*b*12)
eq2 = h*c*12
eq3 = (d*24)+(g*e*12)+(h*f*12)
# Print the answer
print(f"\nProblem 55: She should choose the third job offer, and it is better by ${round(eq3-eq1,2)}")

# ! PROBLEM 56
# What is the inverse of the function y = 2 - sqrt(x)? State the domains of both the function and its inverse.

# * PROBLEM 57
# f(x) = -1.5x + 3; find f(0), solve f(x) = 0, find f^-1(0), and solve f^-1(x) = 0
a, b, c = -1.5, 3, 0
eq1 = a*0+b
eq2 = (c-b)/a
eq3 = (c-b)/a
# Print the answer
print(f"\nProblem 57: f(0) = {eq1}, f(x) = 0 when x = {eq2}, f^-1(0) = {eq3}, and f^-1(x) = 0 when x = {eq2}")

# ! PROBLEM 58

# ! PROBLEM 59

# ! PROBLEM 60

# ! PROBLEM 61