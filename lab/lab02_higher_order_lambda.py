def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC."""

    ###############
    # My Solution #
    ###############

    return lambda x: lambda y: func(x,y)

def count_cond(condition):
    """Returns a function with one parameter N that counts all the numbers from
    1 to N that satisfy the two-argument predicate function Condition, where
    the first argument for Condition is N and the second argument is the
    number from 1 to N."""

    ###############
    # My Solution #
    ###############

    def count_num(n):
        i, count = 1, 0
        while i <= n:
            if condition(n, i) == True:
               count+=1 
            i+=1
        return count
    
    return lambda n: count_num(n)

def compose1(f, g):
    """Return the composition function which given x, computes f(g(x))."""

    ###############
    # My Solution #
    ###############

    return lambda x: f(g(x))

def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa."""

    ###############
    # My Solution #
    ###############

    def is_true(x):
        if f(g(x)) == g(f(x)):
            return True

        return False

    return lambda x: is_true(x)

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function."""

    ###############
    # My Solution #
    ###############

    def cycler(n, x):
        if n == 0:
            return x
        
        result, count = x, 1
        while count <= n:
            if count % 3 == 1:
                result = f1(result)
            elif count % 3 == 2:
                result = f2(result)
            elif count % 3 == 0:
                result = f3(result) 
            count+=1
        
        return result


    return lambda n: lambda x: cycler(n, x)