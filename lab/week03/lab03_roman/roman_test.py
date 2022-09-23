from roman import roman
import pytest

def test():
    assert roman('II') == 2
    assert roman('IV') == 4
    assert roman('XIX') == 19
    assert roman('MDCCLXXVI') == 1776
    assert roman('MMXIX') == 2019
