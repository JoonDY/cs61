def make_adder_inc(a):

    ###############
    # My Solution #
    ###############

    count = 0
    def add(b):
        nonlocal count
        result = a + b + count
        count += 1
        return result

    return add
    


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called."""

    ###############
    # My Solution #
    ###############

    previous, current, count = 0, 1, 0

    def fib():
        nonlocal previous, current, count
        if count == 0:
            count += 1
            return 0
        elif count == 1:
            count+=1
            return 1
        else:
            result = previous + current
            previous, current = current, result
            return result

    return fib
        


def insert_items(lst, entry, elem):

    ###############
    # My Solution #
    ###############
    
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            if entry == elem:
                lst.insert(index, elem)
                index+=1
            else:
                lst.insert(index+1, elem)
                index+=1
        index+=1

    
    return lst