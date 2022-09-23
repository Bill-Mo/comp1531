from permutations import permutations
from hypothesis import given, strategies, assume

def test_permutations():
    assert permutations('ABC') == {'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'}