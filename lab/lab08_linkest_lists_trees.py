def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements."""

    ###############
    # My Solution #
    ###############

    if link == Link.empty:
        return []
    else: 
        return [link.first] + convert_link(link.rest)


def every_other(s):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing)."""

    ###############
    # My Solution #
    ###############

    if s == Link.empty or s.rest == Link.empty:
        return
    else:
        s.rest = s.rest.rest
        every_other(s.rest)


def cumulative_mul(t):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t."""

    ###############
    # My Solution #
    ###############

    if t.is_leaf():
        return
    else:
        for b in t.branches:
                cumulative_mul(b)
                t.label = t.label * b.label


def has_cycle(link):
    """Return whether link contains a cycle."""

    ###############
    # My Solution #
    ###############
    
    def tracker(link, seen = []):
        if link in seen:
            print('True')
            return
        if link.rest == Link.empty:
            print('False')
            return
        seen.append(link)
        tracker(link.rest)


    return tracker(link)

def has_cycle_constant(link):
    """Return whether link contains a cycle."""
    
    ###############
    # My Solution #
    ###############

    one = link
    two = link
    while (two.rest != Link.empty and two.rest.rest != Link.empty):
        one = one.rest
        two = two.rest.rest
        if(one == two):
            return True

    return False


def reverse_other(t):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed."""

    ###############
    # My Solution #
    ###############

    def deep(t, depth):
        depth+=1

        if t.is_leaf():
            return
        
        branches = []
        for b in t.branches:
            branches.append(b.label)
            deep(b, depth)

        branches = branches[::-1]

        if depth % 2 != 0:
            i = 0
            for b in t.branches:
                b.label = branches[i]
                i+=1

    return deep(t, 0)
