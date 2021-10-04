""" Homework 1: Control """

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs."""

    ###############
    # My Solution #
    ###############

    if b >= 0:
        h = add
    else:
        h = sub
    return h(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z."""

    ###############
    # My Solution #
    ###############

    return min(x**2+y**2, x**2+z**2, y**2+z**2)

def largest_factor(x):
    """Return the largest factor of x that is smaller than x."""

    ###############
    # My Solution #
    ###############
    
    i = 2
    factors = [1]
    while i < x:
        if (x % i) == 0:
            factors.append(i)
        i+=1   

    return max(factors)     

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise."""

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
    return False

def t():
    return print(5)

def f():
    return print(6)

def hailstone(x):
    """Print the hailstone sequence starting at x and return its
    length."""

    ###############
    # My Solution #
    ###############

    i = 1
    print(x)
    while x > 1:
        if x % 2 == 0:
            x = x//2
            i+=1
            print(x)
        else:
            x = x*3 + 1
            i+=1
            print(x)

    return i