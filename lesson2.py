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




