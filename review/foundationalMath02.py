# IMPORT LIBRARY FOR CHECKING CODE
import codeTest02 as test

# TEST FOR LIBRARY
test.step01()

# SET WINDOW SIZE TO 20 (VERSION 1)
test.step02('plt.axis([-20, 20, -20, 20])')

# SET WINDOW SIZE TO 20 (VERSION 2)
test.step03('xmax = 20')

# DISPLAY AXIS LINES
test.step04("plt.plot([xmin,xmax],[0,0],'g') plt.plot([0,0],[ymin,ymax], 'g')")

# PLOT A POINT
test.step05("plt.plot([-5],[1],'ro')")

# PLOT POINTS 
test.step06("x = [4, 1, 2] y = [2, 1, 5]")

# PLOT POINTS AND LINES
test.step07("plt.plot(linex,liney,'r') plt.plot(pointx,pointy,'gs')")

# SCATTERPLOT (PLAY GAME)
test.step08("3")

# GRAPH LINEAR EQUATIONS
test.step09("plt.plot(x,-x+3)")

# CREATE INTERACTIVE GRAPH (RUN CODE)
# ! No test

# GRAPH SYSTEMS
test.step11("y2 = -x - 3")

# SYSTEMS OF EQUATIONS
test.step12("print(linsolve([2*x + y - 15, 3*x - y], (x, y)))")

# SOLUTIONS AS COORDINATES (RUN CODE)
# ! No test

# SYSTEMS FROM USER INPUT (RUN CODE)
# ! No test

# SOLVE AND GRAPH A SYSTEM (RUN CODE)
# ! No test

# QUADRATIC FUNCTIONS (RUN CODE)
# ! No test

# QUADRATIC FUNCTION ABC'S
test.step17("def f(a,b,c): plt.plot(x, a*x**2 + b*x + c) interactive_plot = interactive(f, a=(-9, 9), b=(-9,9), c=(-9,9))")

# QUADRADIC FUNCTIONS - VERTEX
test.step18("vx = -b/(2*a) vy = a*vx**2 + b*vx + c")

# PROJECTILE MOTION
test.step19("vx = -b/(2*a) vy = a*vx**2 + b*vx + c ")
# ! No need to change dimensions for test to pass

# QUADRATIC FUNCTIONS - C (RUN CODE)
# ! No test

# QUADRATIC FORMULA
test.step21("x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a) x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)")

# TABLE OF VALUES
test.step22("rows.append([a, 3*a+2])")
# ! No need to change title for test to pass

# PROJECTILE GAME
# ! Refer to projects/projectileGame.py for code

# DEFINE GRAPHING FUNCTIONS AND CERTIFICATION PROJECT 2
# ! Refer to projects/graphingCalculator.py for code