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