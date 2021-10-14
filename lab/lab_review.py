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
