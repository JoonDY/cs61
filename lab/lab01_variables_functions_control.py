def falling(n, k):
    """Compute the falling factorial of n to depth k."""

    ###############
    # My Solution #
    ###############
    
    total = 1
    i = 0
    while i < k:
        total*=n
        n-=1
        i+=1
    
    return total 

def sum_digits(y):
    """Sum all the digits of y."""

    ###############
    # My Solution #
    ###############

    sum = 0
    while y > 0:
        if y == 1:
            sum+=1
        else:    
            sum = sum + (y % 10)
        y = y//10

    return sum

def double_eights(n):
    """Return true if n has two eights in a row."""

    ###############
    # My Solution #
    ###############

    previousNum = 0
    currentNum = 0

    while n > 0:
        if n == 1:
            currentNum = 1
        else:
            currentNum = n % 10

        if previousNum == 8 & currentNum==8:
            previousNum = currentNum   
            return True
         
        previousNum = currentNum  
        n = n//10
         

    return False 