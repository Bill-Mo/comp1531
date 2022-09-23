from divisors import divisors
import pytest
from hypothesis import given, strategies

def test_12():
    assert divisors(12) == {1,2,3,4,6,12}

def test_negative():
    with pytest.raises(ValueError):
        divisors(-2)

def test_prime():
    assert divisors(19) == {1, 19}