# Iteration Sequence

def fib(n):
    """Compute the nth Fibonacci number, for n >= 2."""
    predecessor, current = 0, 1 # first 2 fibonacci numbers
    k = 2, # Tracks which Fibanacci number is called current
    while k < n:
        predecessor, current = current, predecessor + current
        k += 1
    return current


# designing functions
# -----------------------
# characteristics of functions

# -- A functions DOMAIN is the set of all inputs it might possibly take as arguments
# -- A functions RANGE is the set of output values in might possibly return
# -- A funcitons BEHAVIOR is the relationship it creates between input and output

# A guide to designing functions
# -- Give each function exactly one job
# -- Dont repeat yourself (DRY).  Implement just once, execute it many times
# -- Define functions generally



# Higher Order Functions
# ----------------------
# Generalize patterns with arguments
# For example:
# geometric shapes have specific constants that define how area is calculated with respect to r

"""Generalization"""

from math import pi, sqrt

def area_square(r):
    assert r > 0, 'A length must be positive'  # assert statement
    return r * r

def area_circle(r):
    return r * r * pi

def area_hexagon(r):
    return r * r * 3 * sqrt(3) / 2

# assert statement can be used to force certain conditions to exist, if false it will print the error

# but more generally, the above could be simplified and generalized:

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

# and then the other functions would be re-done as

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

# Even more generally, we can generalize computational principles

def sum_naturals(n):
    """Sum the first N natural numbers
    
    >>> sum_naturals(5)
    15
    """
    
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

#  A higher order function take a function as an argument

# here's a function that returns a function

def make_adder(n):
    """Return a function that takes one argument K
    and return K + N.
    
    >>> add_three = make_adder(3)
    >>> add_three(4) 
    7
    """"
    def adder(k):  # the funtion that will be made
        return k + n
    return adder


# The Purpose of higher-order funcitons
# -- FUNCTIONS ARE FIRST CLASS = Functions can be manipulated as values in our 
#    programming language
# -- HIGHER-ORDER FUNCTION: A function that takes a function as an argument or returns
#    a function as a return value

# Higher-Order Functions:
# * Express general methods of computation
# * Remove repetition from programs
# * Seperate concerns among functions

