from lucky import lucky

def test_sample():
    assert lucky(1, 19, 4) == [1,3,7,9,13,15]
    assert lucky(2, 10, 6) == [2, 4, 6, 10]

def test_zero_round():
    assert lucky(1, 5, 0) == [1, 2, 3, 4, 5]
