def insert_into_all(item, nested_list):
    """Assuming that nested_list is a list of lists, return a new list
    consisting of all the lists in nested_list, but with item added to
    the front of each."""

    ###############
    # My Solution #
    ###############

    return [[item] + x for x in nested_list] 


def subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists). The subsequences can appear in any order."""

    ###############
    # My Solution #
    ###############

    if not s:
        return [[]]
    else:
        return insert_into_all(s[0], subseqs(s[1:])) + subseqs(s[1:])


def inc_subseqs(s):
    """Assuming that S is a list, return a nested list of all subsequences
    of S (a list of lists) for which the elements of the subsequence
    are strictly nondecreasing. The subsequences can appear in any order."""

    ###############
    # My Solution #
    ###############

    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b
    return subseq_helper(s, 0)



def num_trees(n):
    """How many full binary trees have exactly n leaves? E.g., """

    ###############
    # My Solution #
    ###############

    if n == 1:
        return 1
    return sum(num_trees(k) * num_trees(n-k) for k in range(1, n))



def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g."""

    ###############
    # My Solution #
    ###############

    def gen(i):
        x = g()
        for _ in range(i):
            yield next(x)

    for i in range(len(list(g()))):
        yield gen(i+1)


class Button:
    """
    Represents a single button
    """
    def __init__(self, pos, key):
        """
        Creates a button
        """
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard takes in an arbitrary amount of buttons, and has a
    dictionary of positions as keys, and values as Buttons."""

    ###############
    # My Solution #
    ###############

    def __init__(self, *args):
        self.buttons = {}
        for arg in args:
            self.buttons[arg.pos] = arg

    def press(self, info):
        """Takes in a position of the button pressed, and
        returns that button's output"""
        if info in self.buttons:
            self.buttons[info].times_pressed += 1
            return self.buttons[info].key
        return ''

    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output"""
        output = ''
        for input in typing_input:
            output += self.press(input)
        return output


def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:"""

    ###############
    # My Solution #
    ###############

    global_count = 0
    def global_counter():
        count = 0
        def local_counter(action):
            nonlocal global_count, count
            if action == 'global-count':
                global_count += 1
                return global_count
            elif action == 'count':
                count += 1
                return count
            elif action == 'global-reset':
                global_count = 0
            elif action == 'reset':
                count = 0
        return local_counter
    return global_counter


def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum."""

    ###############
    # My Solution #
    ###############

    m, n = 1, 1

    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    
    while (m <= len(first) and n <= len(second)) and not equal_prefix():
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1
    
    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'


def card(n):
    """Return the playing card numeral as a string for a positive n <= 13."""
    assert type(n) == int and n > 0 and n <= 13, "Bad card n"
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))

def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards."""

    ###############
    # My Solution #
    ###############

    assert len(cards) % 2 == 0, 'len(cards) must be even'
    half = int(len(cards)/2)
    # shuffled = []
    # for i in range(half):
    #     shuffled.append(cards[i])
    #     shuffled.append(cards[half+i])
    # return shuffled
    
    return sum([[x, y] for (x,y) in zip(cards[:half], cards[half:])], [])


def insert(link, value, index):
    """Insert a value into a Link at the given index."""

    ###############
    # My Solution #
    ###############

    def helper(link, i=0):
        if i == index:
            link.rest = Link(link.first, link.rest)
            link.first = value
            return
        elif link == Link.empty or link.rest == Link.empty:
            raise IndexError
        else:
            helper(link.rest, i+1)
    return helper(link)




def deep_len(lnk):
    """ Returns the deep length of a possibly deep linked list."""

    ###############
    # My Solution #
    ###############

    if lnk == Link.empty:
        return 0
    elif not isinstance(lnk, Link):
        return 1
    else:
        return deep_len(lnk.first) + deep_len(lnk.rest)


def make_to_string(front, mid, back, empty_repr):
    """ Returns a function that turns linked lists to strings."""

    ###############
    # My Solution #
    ###############

    def printer(lnk):
        if lnk == Link.empty:
            return empty_repr
        else:
            return f'{front}{lnk.first}{mid}{printer(lnk.rest)}{back}' 
    return printer


def prune_small(t, n):
    """Prune the tree mutatively, keeping only the n branches
    of each node with the smallest label."""

    ###############
    # My Solution #
    ###############
    
    while len(t.branches) > n:
        largest = max(t.branches, key= lambda x: x.label)
        t.branches.remove(largest)
    for b in t.branches:
        prune_small(b, n)


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

