def factors(num):
    '''
    Returns a list containing the prime factors of 'num'. The primes should be
    listed in ascending order.

    For example:
    >>> factors(16)
    [2, 2, 2, 2]
    >>> factors(21)
    [3, 7]
    '''
    if num == 1:
        return [1]
    l = []
    factor = 2
    while num != 1:
        if num % factor == 0:
            num = num / factor
            is_prime = 0
            l.append(factor)
        if num % factor != 0 or is_prime != 0:
            factor += 1
    return l
