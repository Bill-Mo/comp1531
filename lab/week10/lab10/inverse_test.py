from inverse import inverse
from hypothesis import given, strategies

def test_inverse():
    assert inverse({1: 'A', 2: 'B', 3: 'A'}) == {'A': [1, 3], 'B': [2]}
    assert inverse({'a': 1, 'b': 2, 'c': 3, 'd': 4}) == {1: ['a'], 2: ['b'], 3: ['c'], 4: ['d']}