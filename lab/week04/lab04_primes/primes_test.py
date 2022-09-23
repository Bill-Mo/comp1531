from primes import factors

def test_many():
    assert factors(5436090) == [2, 3, 3, 5, 11, 17, 17, 19]
    
def test_few():
    assert factors(10) == [2, 5]
    
def test_duplicate():
    assert factors(64) == [2, 2, 2, 2, 2, 2]
    
def test_one():
    assert factors(1) == [1]
