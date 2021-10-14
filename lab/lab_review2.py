def prune_min(t):
    """Prune the tree mutatively from the bottom up."""

    ###############
    # My Solution #
    ###############

    if t.is_leaf():
        return
    else:
        if t.branches[0].label < t.branches[1].label:
            t.branches = [t.branches[0]]
            prune_min(t.branches[0])
        else:
            t.branches = [t.branches[1]]
            prune_min(t.branches[1])



def num_splits(s, d):
    """Return the number of ways in which s can be partitioned into two
    sublists that have sums within d of each other."""

    ###############
    # My Solution #
    ###############

    def helper(s, diff):
        
        if len(s) == 0:
            print(diff)
            if abs(diff) <= d:
                return 1
            else:
                return 0
        else:
            # yes = helper(s[1:], sum1 + s[0], sum2)
            # no = helper(s[1:], sum1, sum2 + s[0])
            # return yes + no
            return helper(s[1:], diff + s[0]) + helper(s[1:], diff - s[0])
        
    return helper(s, 0) // 2 


class Account(object):
    """A bank account that allows deposits and withdrawals."""

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        """Increase the account balance by amount and return the
        new balance.
        """
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the
        new balance.
        """
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance

class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""

    ###############
    # My Solution #
    ###############

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self, check):
        if check.payable == self.holder and check.deposited == False:
            Account.deposit(self, check.amount)
            check.deposited = True
            print(check.amount)
        else:
            print('The police have been notified.')


class Check(object):

    ###############
    # My Solution #
    ###############

    def __init__(self, payable, amount):
        self.payable = payable
        self.amount = amount
        self.deposited = False



def align_skeleton(skeleton, code):
    """
    Aligns the given skeleton with the given code, minimizing the edit distance between
    the two. Both skeleton and code are assumed to be valid one-line strings of code. """

    ###############
    # My Solution #
    ###############

    skeleton, code = skeleton.replace(" ", ""), code.replace(" ", "")

    def helper_align(skeleton_idx, code_idx):
        """
        Aligns the given skeletal segment with the code.
        Returns (match, cost)
            match: the sequence of corrections as a string
            cost: the cost of the corrections, in edits
        """
        if skeleton_idx == len(skeleton) and code_idx == len(code):
            return '', 0

        if skeleton_idx < len(skeleton) and code_idx == len(code):
            edits = "".join(["-[" + c + "]" for c in skeleton[skeleton_idx:]])
            return edits, len(skeleton) - skeleton_idx

        if skeleton_idx == len(skeleton) and code_idx < len(code):
            edits = "".join(["+[" + c + "]" for c in code[code_idx:]])
            return edits, len(code) - code_idx
        
        possibilities = []
        skel_char, code_char = skeleton[skeleton_idx], code[code_idx]
        # Match
        if skel_char == code_char:
            match_result, match_cost = helper_align(skeleton_idx+1, code_idx+1)
            match_total = skel_char + match_result
            possibilities.append((match_total, match_cost))
        # Insert
        insert_result, insert_cost = helper_align(skeleton_idx, code_idx+1)
        insert_total = "+[" + code_char + "]" + insert_result
        possibilities.append((insert_total, insert_cost+1))
        # Delete
        delete_result, delete_cost = helper_align(skeleton_idx+1, code_idx)
        delete_total = "-[" + skel_char + "]" + delete_result
        possibilities.append((delete_total, delete_cost+1))
        return min(possibilities, key=lambda x: x[1])
    result, cost = helper_align(0, 0)
    return result


def foldl(link, fn, z):
    """ Left fold"""

    ###############
    # My Solution #
    ###############

    if link is Link.empty:
        return z
    return foldl(link.rest, fn, fn(z, link.first))


def filterl(lst, pred):
    """ Filters LST based on PRED"""

    ###############
    # My Solution #
    ###############

    if lst is Link.empty:
        return lst
    else:
        if pred(lst.rest.first):
            filterl(lst.rest, pred)
        else:
            lst.rest = lst.rest.rest
            filterl(lst.rest, pred)    
    return lst


def reverse(lst):
    """ Reverses LST with foldl"""

    ###############
    # My Solution #
    ###############

    if lst == Link.empty:
        return lst

    lnk = Link(lst.first)
    while lst.rest is not Link.empty:
        lst = lst.rest
        lnk = Link(lst.first, lnk)
    return lnk
