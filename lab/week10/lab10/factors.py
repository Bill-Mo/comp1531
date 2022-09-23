'''
NOTE: This exercise assumes you have completed divisors.py
'''

from divisors import divisors

# You may find this helpful
def is_prime(n):
    return n != 1 and divisors(n) == {1, n}

def factors(n):
    '''
    A generator that generates the prime factors of n. For example
    >>> list(factors(12))
    [2,2,3]

    Params:
      n (int): The operand

    Yields:
      (int): All the prime factors of n in ascending order.

    Raises:
      ValueError: When n is <= 1.
    '''
    for f in divisors(n):
      print(f"if {f} is prime")
      if is_prime(f) and len(divisors(n)) != 1:
        print(f"{f} is prime")
        yield f
        n = int(n / f)
        print(n)
        
print(list(factors(12)))
