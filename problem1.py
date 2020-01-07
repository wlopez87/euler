# -*- coding: utf-8 -*-
"""
Project Euler - Problem 1
Multiples of 3 and 5

If we list all the natural numbers below
10 that are multiples of 3 of 5, we get
3, 5, 9. The sum of these multiples is 23.

Find the sum of all multiples of 3 or 5
below 1000.

"""
is_mult_of_3_or_5 = lambda n: n%3 == 0 or n% 5 == 0

def solve(n):
    """
    >>> solve(10)
    23
    """
    xs = range(1, n)
    return sum(filter(is_mult_of_3_or_5, xs))

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(solve(1000))

