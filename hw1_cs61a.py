# Homework 1 

from operator import add, sub
def a_plus_abs_b(a,b):
    """Return a+abs(b), but without calling abs.
    
    >>> a_plus_abs_b(2,3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        op = sub
    else:
        op = add
    return op(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x, y are the 2 largest of A,B,C.
    
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    """
    
    if(a > c) and (b > c):
        return a*a + b*b
    elif(b > a) and (c > a):
        return b*b + c*c
    else:
        return a*a + c*c

def two_of_three_v2(a, b, c):
    """Return x*x + y*y, where x, y are the 2 largest of A,B,C.
    EXCEPT without using Boolean expressions
    
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    """
    
    return max(a,b,c)*max(a,b,c) + ((a+b+c)-max(a,b,c)-min(a,b,c))^2

def benchmark(cycles):
    from random import randint
    from time import perf_counter
    
    i = 0
    
    print('starting perf_counter V1...')
   
    start = perf_counter()
    while i < cycles:
        a, b, c = randint(1,1000), randint(1,1000), randint(1,1000)
        two_of_three(a, b, c)
        i += 1
    stop = perf_counter()
    
    print('Benchmark counter v1: ', stop - start)
 
 # try it again using other funtion 
 # (OK, so not exactly DRY-compliant)
   
    i = 0
    
    print('starting per_counter V2...')
    
    start = perf_counter()
    while i < cycles:
        a, b, c = randint(1,1000), randint(1,1000), randint(1,1000)
        two_of_three(a, b, c)
        i += 1
    stop = perf_counter()
    print('Benchmark counter v2:', stop - start)
    
    return

    