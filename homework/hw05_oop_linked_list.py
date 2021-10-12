class VendingMachine:
    """A vending machine that vends some product for some price."""

    ###############
    # My Solution #
    ###############

    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.fund = 0
    
    def add_funds(self, amount):
        if not self.stock:
            return f'Inventory empty. Restocking required. Here is your ${amount}.'
        self.fund += amount
        return f'Current balance: ${self.fund}'
        

    def vend(self):
        if not self.stock:
            return 'Inventory empty. Restocking required.'
        elif self.fund < self.price:
            return f'You must add ${self.price - self.fund} more funds.'
        elif self.fund > self.price:
            self.stock -= 1
            refund = self.fund - self.price
            self.fund = 0
            return f'Here is your candy and ${refund} change.'
        else:
            self.stock -= 1
            self.fund = 0
            return f'Here is your {self.product}.'

    
    def restock(self, amount):
        self.stock += amount
        return f'Current {self.product} stock: {self.stock}'


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year."""

    ###############
    # My Solution #
    ###############

    current_year = 2020

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        self.year = self.current_year

class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        return max(Mint.current_year - self.year - 50, 0) + self.cents

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list."""

    ###############
    # My Solution #
    ###############

    def helper(n, other):
        if n // 10 == 0:
            return Link(n, other)
        else:
            return helper(n // 10, Link(n % 10, other)) 

    return helper(n, Link.empty)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST."""

    ###############
    # My Solution #
    ###############

    def helper(t, bst_min, bst_max):
        if t.is_leaf(): 
            if bst_min < t.label <= bst_max:
                return True
            else: 
                return False
        else:
            if len(t.branches) > 2:
                return False
            elif len(t.branches) == 2:                     
                for b in t.branches:
                    if b == t.branches[0] and bst_min < b.label<= t.label:
                        return helper(b, bst_min, t.label)
                    if b == t.branches[1] and bst_max >= b.label > t.label:
                        return helper(b, t.label, bst_max)
                    else:
                        return False
            elif len(t.branches) == 1:
                    return helper(t.branches[0], bst_min, bst_max)

    return helper(t, float('-inf'), float('inf'))

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description)."""

    ###############
    # My Solution #
    ###############

    def helper(t, result = []):
        result.append(t.label)
        for b in t.branches:
            helper(b, result)
        return result
    return helper(t)


def path_yielder(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list."""

    ###############
    # My Solution #
    ###############

    path = []
    path.append(t.label)
    
    if t.label == value:
        yield path

    for b in t.branches:
        for p in path_yielder(b, value):
            yield path + p
            

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