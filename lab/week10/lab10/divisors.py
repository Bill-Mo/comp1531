def divisors(n):
    '''
    Given some number n, return a set of all the numbers that divide it. For example:
    >>> divisors(12)
    {1, 2, 3, 4, 6, 12}

    Params:
      n (int): The operand

    Returns:
      (set of int): All the divisors of n

    Raises:
      ValueError: If n is not a positive integer
    '''
    if n <= 0:
      raise ValueError("n is not a positive integer.")
    s = set()
    div = 0
    for div in range(1, n + 1):
      if n % div == 0:
        s.add(div)
        
    return s
