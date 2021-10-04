def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be a arm"
    assert is_arm(right), "right must be a arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct a arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is a arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of a arm."""
    assert is_arm(s), "must call length on a arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of a arm."""
    assert is_arm(s), "must call end on a arm"
    return s[2]

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

def is_planet(w):
    """Whether w is a planet."""
    return type(w) == list and len(w) == 2 and w[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                              arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return (t, u, v)

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

def interval(a, b):
    """Construct an interval from a to b."""
    return [a, b]

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

def str_interval(x):
    """Return a string representation of interval x.
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y."""
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

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

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

def check_par():
    """Return two intervals that give different results for parallel resistors."""

    ###############
    # My Solution #
    ############### 

    r1 = interval(-2, -1) 
    r2 = interval(-2, -1) 
    return r1, r2

def multiple_references_explanation():
    return """The multiple reference problem..."""

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

# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])