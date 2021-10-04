def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]]."""

    ###############
    # My Solution #
    ###############

    assert len(s) == len(t)

    new_list = []
    for i in range(0, len(s)):
        new_list.append([s[i]] + [t[i]])
    
    return new_list


from math import sqrt

def distance(city_a, city_b):

    ###############
    # My Solution #
    ###############

    city1 = [get_lat(city_a),get_lon(city_a)]
    city2 = [get_lat(city_b),get_lon(city_b)]

    return sqrt((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)

def closer_city(lat, lon, city_a, city_b):
    """
    Returns the name of either city_a or city_b, whichever is closest to
    coordinate (lat, lon). If the two cities are the same distance away
    from the coordinate, consider city_b to be the closer city.
    """

    ###############
    # My Solution #
    ###############
    
    start = make_city('start', lat, lon)
    result = distance(start, city_b) <= distance(start, city_a)

    if result:
        return get_name(city_b)
    else:
        return get_name(city_a)



def make_city(name, lat, lon):
    if change_abstraction.changed:
        return {"name" : name, "lat" : lat, "lon" : lon}
    else:
        return [name, lat, lon]

def get_name(city):
    if change_abstraction.changed:
        return city["name"]
    else:
        return city[0]

def get_lat(city):
    if change_abstraction.changed:
        return city["lat"]
    else:
        return city[1]

def get_lon(city):
    if change_abstraction.changed:
        return city["lon"]
    else:
        return city[2]

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise."""

    ###############
    # My Solution #
    ###############

    if label(t) == 'berry':
        return True
    else:
        for b in branches(t):
            if berry_finder(b) == True:
                return True
        return False



def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree."""

    ###############
    # My Solution #
    ###############

    if is_leaf(t):
        new_leaves = []
        for leaf in leaves:
            new_leaves.append(tree(leaf))
        return tree(label(t), new_leaves)
    else:
        new_branches = [sprout_leaves(b, leaves) for b in branches(t)]
        return tree(label(t), new_branches)



def coords(fn, seq, lower, upper):

    ###############
    # My Solution #
    ###############

    return [[x]+[fn(x)] for x in seq if fn(x) <= upper and fn(x) >= lower]



def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even."""

    ###############
    # My Solution #
    ###############

    # result = []
    # for card in range(0, int(len(deck)/2)):
    #     result += [deck[card]] + [deck[(card+int(len(deck)/2))]]

    # return result

    return sum([[deck[card]] + [deck[(card+int(len(deck)/2))]] for card in range(0, int(len(deck)/2))], [])



def add_trees(t1, t2):

    ###############
    # My Solution #
    ###############

    len_t1, len_t2 = len(branches(t1)), len(branches(t2))
    if len_t1 == len_t2:
        return tree(label(t1) + label(t2), [add_trees(b1, b2) for b1, b2 in zip(branches(t1), branches(t2))])
    elif len_t1 < len_t2:
        branches_t1 = branches(t1) + [tree(0) for _ in range(len_t2 - len_t1)]
        new_t1 = tree(label(t1), branches_t1)
        return add_trees(new_t1, t2)
    else:
        return add_trees(t2, t1)

          

def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors."""

    ###############
    # My Solution #
    ###############

    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:    
            table[prev] = table[prev] + [word]
        prev = word
    return table



def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table."""

    ###############
    # My Solution #
    ###############

    import random
    result = ''
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result.strip() + word



def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open(path, encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()


tokens = shakespeare_tokens()
table = build_successors_table(tokens)


def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)


# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
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

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


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

