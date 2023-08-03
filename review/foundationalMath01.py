# IMPORT LIBRARY FOR CHECKING CODE
import codeTest01 as test

# ADDITION
test.step01('print(a+b)')

# SUBTRACTION
test.step02('print(c-d)')

# MULTIPLICATION
test.step03('print(e*f)')

# DIVISION
test.step04('print(g/h)')

# CASTING
test.step05('intB = int(strB)')

# INPUT AND CAST ON THE SAME LINE
test.step06('intB = int(input(\'Enter an integer: \'))')

# FLOAT NUMBERS
test.step07("b = float(input('Enter a number: '))")

# ORDER OF OPERATIONS
test.step08(8)

# REMAINER AND MODULUS
test.step09('print(a%b)')

# MODULUS AND FACTORS
test.step10("if number % test_factor == 0: print('true') else: print('false')")

# FINDING FACTORS
test.step11("for test_factor in range(1, number+1): if number % test_factor == 0: print('true') else: print('false')")

# PRIME NUMBERS
test.step12("for test_number in range(2, number): if number % test_number == 0: print('true') else: print('false')")

# RECIPROCALS
test.step13("print(1/n)")

# SPLITTING INPUT
test.step14("b = float(sp[1]) print(a/b)")

# SQUARE NUMBERS
test.step15("print(n**2)")

# SQUARE ROOTS
test.step16("print(math.sqrt(n))")

# FLOOR FUNCTION
test.step17("print(math.floor(n))")

# FINDING SQUARE FACTORS
test.step18("for maybe_factor in range(1,upper_limit): if n % (maybe_factor**2) == 0: max_factor = maybe_factor")

# ! STEPS 19 to 20 does not need input

# ROUNDING
test.step21("print(round(a,-6)) print(round(b,3)")

# FRACTIONS, DECIMALS, PERCENTS
n = 0.123456789 # ! Sample value
exponent = 2 # ! Sample value
# * Answer:
numerator = int(n*10**exponent)
denominator = 10**exponent
percent = n*100
test.step22(n, numerator, denominator, percent, exponent)

# DEFIINING A FUNCTION
# * Answer:
def fun():
    print("This is in the function")
# Other code not in the function
print("This is outside the function")
# Call the function
fun()

print("Back outside the function")

# FUNCTION WITH INPUT
# * Answer:
# Define a function
def greeting(name):
    print("Hello ", name)
nombre = 'World' # ! Sample value
# Call the function
greeting(nombre)

# FUNCTION WITH TWO INPUTS
# * Answer:
# Define function
def add(a,b,c):
  # Use c for the third variable
  sum = a+b+c
  print("The sum is ", sum)
first = 1 # ! Sample value
second= 2 # ! Sample value
third = 3
# Call the function
add(first,second,third)

# FUNCTION WITH RETURN
test.step26("return number*3")

# STEPS 27 to 30 does not have tests