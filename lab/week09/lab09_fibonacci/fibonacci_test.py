from fibonacci import generate

def test_empty():
    assert generate(0) == []

def test_not_num():
    assert generate('[') == []
    assert generate('apple') == []

def test_fibonacci():
    assert generate(1) == [0]
    assert generate(2) == [0, 1]
    assert generate(3) == [0, 1, 1]
    assert generate(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
