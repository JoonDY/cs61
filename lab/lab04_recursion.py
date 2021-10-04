def skip_add(n):
    """ Takes a number n and returns n + n-2 + n-4 + n-6 + ... + 0."""

    ###############
    # My Solution #
    ###############

    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)

def summation(n, term):

    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion!"""

    ###############
    # My Solution #
    ###############

    assert n >= 1

    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)

def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner."""

    ###############
    # My Solution #
    ###############

    if m == 1:
        return 1
    elif n == 1:
        return 1
    else:
        up = paths(m-1, n)
        right = paths(m, n-1)
        return up + right

def max_subseq(n, t):
    """
    Return the maximum subsequence of length at most t that can be found in the given number n.
    For example, for n = 20125 and t = 3, we have that the subsequences are"""

    ###############
    # My Solution #
    ###############

    if n == 0 or t == 0:
       return 0
    yes = max_subseq(n//10, t-1) * 10 + n % 10
    no = max_subseq(n//10, t)
    print(yes, no)
    if yes > no:
        return yes
    else:
        return no

def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.

    You may assume that w1 is a subsequence of w2."""

    ###############
    # My Solution #
    ###############

    # w1 = list(w1)
    # w2 = list(w2)

    # for i in w1:
    #     for j in w2:
    #         if i == j:
    #             w2.remove(j)
    #             break
    
    # print(w2)

    if len(w1) == 0 or len(w2) == 0:
        return w2
    else:
        if w1[0] == w2[0]:
            return add_chars(w1[1:], w2[1:])
        else:
            return w2[0] + add_chars(w1, w2[1:])            