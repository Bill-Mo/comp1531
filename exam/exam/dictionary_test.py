from dictionary import construct_dict
import pytest

def test_sample():
    l1 = ['a', 'b', 'c']
    l2 = [1, 2, 3]
    assert(construct_dict(l1, l2) == {'a': 1, 'b': 2, 'c': 3})

def test_repeat():
    assert(construct_dict(['a', 'b', 'b'], [1, 2, 3]) == {'a': 1, 'b': 3})
    
def test_error():
    with pytest.raises(ValueError):
        l1 = ['a', 'b', 'c', 'd']
        l2 = [1, 2, 3]
        construct_dict(l1, l2)
