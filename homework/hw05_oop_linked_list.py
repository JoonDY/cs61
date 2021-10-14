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