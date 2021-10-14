def planet(size):
    """Construct a planet of some size."""

    ###############
    # My Solution #
    ###############

    assert size > 0
    return ['planet', size]

def size(w):
    """Select the size of a planet."""

    ###############
    # My Solution #
    ###############

    assert is_planet(w), 'must call size on a planet'
    return w[1]

def total_weight(m):
    """Return the total weight of m, a planet or mobile."""

    ###############
    # My Solution #
    ###############

    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))

def balanced(m):
    """Return whether m is balanced."""

    ###############
    # My Solution #
    ###############

    if is_planet(m):
        return True

    left_w = total_weight((end(left(m))))
    right_w = total_weight((end(right(m))))   
    if not ((left_w * length(left(m))) == (right_w * length(right(m)))):
        
        return False
    else:
        return balanced(end(left(m))) and balanced(end(right(m)))  

def totals_tree(m):
    """Return a tree representing the mobile with its total weight at the root."""

    ###############
    # My Solution #
    ###############
    
    if is_planet(m):
        return tree(size(m))
    if is_mobile(m):
        l_branch = tree(totals_tree(end(left(m))))
        r_branch = tree(totals_tree(end(right(m))))
        branch = sum([l_branch,r_branch], [])
        return tree(total_weight(m), branch)

def replace_leaf(t, find_value, replace_value):
    """Returns a new tree where every leaf value equal to find_value has
    been replaced with replace_value."""

    ###############
    # My Solution #
    ###############

    if is_leaf(t):
        if label(t) == find_value:
            return tree(replace_value)
        else:
            return tree(label(t))
    else:
        branch = [replace_leaf(b, find_value, replace_value) for b in branches(t)]
        return tree(label(t), branch)

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description)."""
    
    ###############
    # My Solution #
    ############### 
       
    results = []
    def accumulator(t, total):
        total.append(label(t))
        for b in branches(t):
            accumulator(b, total)
        return results
    
    return accumulator(t, results)   

def has_path(t, word):
    """Return whether there is a path in a tree where the entries along the path
    spell out a particular word."""

    ###############
    # My Solution #
    ############### 

    assert len(word) > 0, 'no path for empty word.'
    
    def accumulator(t, total, results):
        total = total + label(t)
        if is_leaf(t):
            results.append(total)
        else:
            for b in branches(t):
                accumulator(b, total, results)
        return word in results
                
    return accumulator(t, '', [label(t)])

def lower_bound(x):
    """Return the lower bound of interval x."""

    ###############
    # My Solution #
    ############### 

    return min(x)

def upper_bound(x):
    """Return the upper bound of interval x."""

    ###############
    # My Solution #
    ############### 

    return max(x)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y."""

    ###############
    # My Solution #
    ############### 

    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y."""

    ###############
    # My Solution #
    ############### 


    lowest = lower_bound(x) - upper_bound(y)
    highest = upper_bound(x) - lower_bound(y)
    return interval(lowest, highest)

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by
    any value in y. Division is implemented as the multiplication of x by the
    reciprocal of y."""

    ###############
    # My Solution #
    ############### 

    assert (upper_bound(y) > 0 and lower_bound(y) > 0) or (upper_bound(y) < 0 and lower_bound(y) < 0)
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def check_par():
    """Return two intervals that give different results for parallel resistors."""

    ###############
    # My Solution #
    ############### 

    r1 = interval(-2, -1) 
    r2 = interval(-2, -1) 
    return r1, r2

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x."""

    ###############
    # My Solution #
    ############### 
    
    def quad(num):
        return a*(num**2) + b*num + c

    apex = -b / (2*a)  
    upper = quad(upper_bound(x))
    lower = quad(lower_bound(x))
    peak = quad(apex)

    if lower_bound(x) < apex < upper_bound(x):
        return interval(min(upper, lower, peak), max(upper, lower, peak))
    else:
        return interval(min(upper, lower), max(upper,lower))