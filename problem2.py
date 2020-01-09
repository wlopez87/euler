# -*- coding: utf-8 -*-

"""
Project Euler - Problem 2
Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1
and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose
values do no exceed four million, find the sum of the
even-valued terms.

"""
def isEven(n):
    """
    >>> isEven(2)
    True
    >>> isEven(3)
    False
    >>> isEven(4)
    True

    """
    return n % 2 == 0

def fibonacci(n):
    """
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(8)
    21
    >>> fibonacci(10)
    55
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def solve(n):
    """
    >>> solve(10)
    44
    >>> solve(11)
    44
    >>> solve(25)
    60696
    """
    xs = range(1, n+1)
    return sum(filter(isEven, map(fibonacci, xs)))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    print(solve(4000000))


