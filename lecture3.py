# CS61A - Lecture 3

# Multiple Environments
#  
# Life Cycle of user defined functions:
# -- Def Statement:
#     Has Name, Formal Parameter, Body
# -- What Happens?
#     A new function is created
#     Name bound to that function in the current frame
# 
# -- Call Expression:
#     Operator and Operands evaluated
#     Function (value of operator) is called on arguments (values of operands)
# 
# -- Calling / Applying
#     A new frame is created
#     Parameters are bound to arguements
#     Body is executed in new environment

from operator import mul
def square(x):
    return mul(x, x)
print(square(square(3)))

# An environment is a sequence of frames
# So Far:
#     - The global frame alone
#     - A local frame, then the global frame
#     - All environments end in the global frame
#     
# 
# Every expression is evaluated in the context of an environment
# 
# A NAME evaluates to the value bound to that name in the earliest
# frame of the current environment in which that name is found.
# 
# --> Video 3 Starts here <--
# ---------------------------
# 
# Operators, Multiple Return Values, Docstrings, Doctests, Default Arguments
# 
# Operators:
# Infix operators obey operator precedence rules
# Parens can override std precedence
# 
# Operators behave as standard function calls
# 
# Division:
# 2010 / 10 = true division
# 2010 // 10 = integer
# 
# have functions:
# from operator import truediv, floordiv
# 
# mod operator: 
2013 % 10
# from operator import mod
mod(2013, 10)
# 
# You can return multiple values from a function:
# 
def divide_exact(n, d):
   return n // d, n % d
# 
# quotient, remainder = divide_exact(2013, 10)
# 
# 
# DOCSTRINGS:
# At top of file, start with """  stuff, stuff, stuff """
# 
# to execute from shell:
# 
# >>> python3 file_name.py

# -or-
# 
# >>> python3 -i file_name.py
# 
# When you write functions, you give some documentation in docstring
# Convention of using all caps to refer to formal parameters
# 
# ~~~~~~~~~~~~~~~~

"""Our first python source file"""

from operator import floordiv, mod

def divide_exact(n, d):
    """Return the quotient and remainder of dividing N by D.
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """
    
    return floordiv(n, d), mod(n, d)

# Note the docstring and doctest.  To run the doctest:
# 
# $ python3 -m doctest file_name.py    -or-
# $ python3 -m doctest -v file_name.py  (w/ verbose flag)

# Default arguments:
# 
# set up default value with formal parameters:

def divide_exact(n, d=10):
    
# default value for parameter will be 10

# 
# --> Video 4 starts here <--
# ---------------------------
# 
# Conditional Statements
# 
# A statement is executed by interpreter to perform an action
# 
# Statement can have more than one line
# 
# <header>:
#     <statement>   
#     <statement>
# <separating header>:
#     <statement>   
#     <statement>
#     
# Conditional statement example:

def absolute_value(x):
    """Return the absolute value of x"""
    if x < 0:
        return -x
    elif x = 0:
        return 0
    else:
        return x

# Above is:
#     1 statement
#     3 clauses
#     3 headers
#     3 suites
# 
# Execution rules for conditional statements
#     Each clause is considered in order
#     1. Evaluate the header expression
#     2. If it is true, execute the suite and skip the remaining clauses
#     
# Always starts with if
# zero or more elifs
# zero or more else
# 
# Iteration
# ----------
# 
# while statement is way to perform iteration

i, total = 0, 0
while i < 3:
    i = i + 1
    total = total + i


# Example:

def choose(total, selection):
    """Return the number of ways to choose SELECTION items from TOTAL.
    
    choose(n,k) is typically defined in math as: n! / (n - k)! / k!
    
    >>> choose(5,2)
    10
    >>> choose(20, 6)
    38760
    """
    ways = 1
    selected = 0
    
    while selected < selection:
        selected = selected + 1
        ways, total = ways * total // selected, total - 1
    return ways

# Start Question 3 here #

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and false_result otherwise."""
    if condition:
        return true_result
    else:
        return false_result
    
def with_if_statement():
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    return 1 > 0

def t():
    return 1

def f():
    return 0

