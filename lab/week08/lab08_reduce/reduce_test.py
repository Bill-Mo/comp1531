from reduce import reduce

def test_empty_or_one():
    assert reduce(lambda x, y: x + y, []) == None
    assert reduce(lambda x, y: x + y, [2]) == 2

def test_sum():
    assert reduce(lambda x, y: x + y, [5, 6, 7, 8]) == 26

def test_mul():
    assert reduce(lambda x, y: x * y, [3, 3, 3, 3]) == 81

def test_power():
    assert reduce(lambda x, y: x ** y, [2, 2, 2, 2]) == 256

def test_join():
    assert reduce(lambda x, y: x + y, ['Today ', 'is ', 'a ', 'wonderful ', 'day!']) == 'Today is a wonderful day!'
