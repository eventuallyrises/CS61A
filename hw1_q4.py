"""Hailstone Sequence problem"""

def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.

    >>> a = hailstone(10)  # Seven elements are 10, 5, 16, 8, 4, 2, 1
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    assert n > 0, 'Seed number %d is not greater than 0' % n    
    assert type(n) == int, 'Seed number is not an Integer'
    count = 1
    while n != 1:
        print(n)
        if(n % 2 == 0):  # N is even
            n = n // 2
        else:        # N is odd
            n = (n * 3) + 1
        count += 1
    print(n)
    return count

        
        