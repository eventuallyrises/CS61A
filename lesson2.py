# Berkeley 61A Fall 2013
# Lesson 2 Notes
# Vaughan Schmidt

# Names, Assignments, User-Defined statements

# to access built-in names, use import statement
from math import pi

# math is module

print(pi)
print(pi * 71 / 223)

# or use an assingment statement to bind values
radius = 10
print('radius: ', radius)

area, circumference = pi * radius * radius, 2 * pi * radius
print('area:', area)
print('circumference:', circumference)

# a function is also a name
print(max)
f = max  # now f is built=in max
print('max of 3,4:',f(3,4))

# you can rename functions
max = 7
# now max is no longer a function, it is value 7
print(max)

print('max of 3, max:', f(3,max))

from operator import add, mul

# can define your own function
def square(x):   # x is formal parameter
    return mul(x, x)   # returns x * x using built in func mul

print(square(3))
print(square(square(3)))

# you can write functions that call other functions
def sum_squares(x, y):
    return add(square(x), square(y))

print('sum of squares 5 & 7:', sum_squares(5,7))

# Summary of video 1:
# Types of expressions:
#     PRIMITIVE EXPRESSIONS
#         2 -> Numeral
#         add -> Name
#         'hello' -> string
#     CALL EXPRESSIONS
#         max(2, 3) --> Call Expression
#          ** An operator could also be a call expression


# --> Lecture 2 Video 3 Starts Here <--
# *************************************
# Environment Diagrams
# --> There to visualize interpreters prcoess
# --> code on left, frames on right
#
# Frames show relationships (bindings) beween name and values
# Within a frame, a name can not be repeated
# Each name is bound to a value
#
# use tutor.composingprograms.com as visualizer
#
# Execution rule for assignment statements
# 1. Evaluate all expressions to right of = from left to right
# 2. Bind all the names to the left of = to the resulting values in current frame


# --> Lecture 2 Video 4 Starts Here <--
# *************************************
# Assignment is a simple means of abstraction: binds names to values
# Function definition is a more powerful abstraction: binds names to expressions

# use def statement to define function
# generically:
# def <name>(<formal parameters>):
#     return <return expression>

# Function signature indicates how many arguments a funtion takes
# Funciotn body defines the computational process expressed by the function

# Procedure for execution of function
# 1. Create a function with signature <name>(<formal parameters>)
# 2. Set the body of that function to be everything indented after the first line
# 3. Bind <name> to that function in the current frame


# Procedure for calling/applying a user-defined function
# 1. Add a local frame, forming a new environment
# 2. Bind the function's formal parameters to its arguments in that frame
# 3. Execute the body of the function in that new environment

# Looking up names in Environments
# - Every expression is evaluated in the context of an environment
# - So far, the current environment is either:
#    a. The global frame alone
#    b. A local frame followed by the global frame
#    
# The most important things:
# - An environment is a sequence of frames
# - A name evaluates to the value bound to that name in the earliest frame
#   of the current environment in which that name is found
# - e.g., to look up some name in the body of the square example function:
#    * look for that name in the local frame
#    * if not found, look for it in the global frame (built-in names are in global environment)

def squared(squared):
    return mul(squared, squared)

