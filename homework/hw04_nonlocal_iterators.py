def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits."""

    ###############
    # My Solution #
    ###############
    
    def bank(message, amount):
        nonlocal balance
        if message == 'deposit':
            balance += amount
            return balance
        elif message == 'withdraw':
            if amount > balance:
                return 'Insufficient funds'
            balance -= amount
            return balance
        else:
            return 'Invalid message'
    
    return bank

def make_withdraw(balance, password):
    """Return a password-protected withdraw function."""

    ###############
    # My Solution #
    ###############

    attempts = []
    frozen = False

    def withdraw(amount, entered):
        nonlocal balance, password, attempts, frozen

        if frozen:
            return 'Frozen account. Attempts: ' + str(attempts) 
        
        if entered == password:
            if amount > balance:
                return 'Insufficient funds'
            balance -= amount
            return balance

        if len(attempts) >= 2:
            frozen = True

        attempts.append(entered)
        return 'Incorrect password'

    return withdraw

def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first."""

    ###############
    # My Solution #
    ###############

    assert k > 1

    count = 1
    prev = 0
    current = 0
    while True:
        current = next(t)
        if current == prev:
            count+=1
        else:
            count = 1

        if count >= k:
            return current
        prev = current
        
def permutations(seq):
    """Generates all permutations of the given sequence. Each permutation is a
    list of the elements in SEQ in a different order. The permutations may be
    yielded in any order."""

    ###############
    # My Solution #
    ###############

    seq = list(seq)
    
    if len(seq) <=1:
        yield seq
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(seq)):
                yield perm[:i] + seq[0:1] + perm[i:]

def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw."""

    ###############
    # My Solution #
    ###############

    passwords = []

    def joint(amount, password, history=passwords):
        if password in history:
            return withdraw(amount, history[0])
        return withdraw(amount, password)

    result = withdraw(0, old_pass)
    if type(result) == str:
        return result
    passwords.extend([old_pass, new_pass])
    return joint

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1."""
    i = 1
    while True:
        yield i
        i += 1

def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m."""

    ###############
    # My Solution #
    ###############

    def generator(i):
        numbers = naturals()
        for num in numbers:
            if num % m == i:
                yield num

    for i in range(0, m):
        yield generator(i)