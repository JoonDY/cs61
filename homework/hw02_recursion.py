def num_eights(x):
    """Returns the number of times 8 appears as a digit of x."""

    ###############
    # My Solution #
    ###############

    if x < 10: 
        if x == 8:
            return 1
        else:
            return 0
    else:
        if x % 10 == 8:
            return num_eights(x//10) + 1
        else:
            return num_eights(x//10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence."""

    ###############
    # My Solution #
    ###############
        
    def helper(result=1, i=1, direction=1):
        if i == n:
            return result

        if i % 8 == 0 or num_eights(i):
            return helper(result - direction, i +1 , -direction)
            
        else:
            return helper(result + direction, i + 1, direction)    


    return helper()

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n."""

    ###############
    # My Solution #
    ###############

    # With helper function

    # def helper(previous, current, count, n):
    #     if n == 0:
    #         return count  
    #     else:
    #         if (previous-current) > 1:
    #             count += (previous - current) -1
    #             return helper(n%10, n//10%10, count, n//10)
    #         else:
    #             return helper(n%10, n//10%10, count, n//10)
    # return helper(0, 0, 0, n)  

    if n < 10:
        return 0
    else:
        if ((n % 10) - (n//10%10)) > 1:
            return ((n % 10) - (n//10%10) - 1) + missing_digits(n//10)
        else:
            return missing_digits(n//10)

def next_largest_coin(coin):
    """Return the next coin."""

    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smallest_coin(coin):

    ###############
    # My Solution #
    ###############

    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25."""

    ###############
    # My Solution #
    ###############

    def helper(total, coin):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif coin == None:
            return 0
        else:    
            current_coin = helper(total - coin, coin)
            next_coin = helper(total, next_smallest_coin(coin))
            return current_coin + next_coin

    return helper(total, 25)