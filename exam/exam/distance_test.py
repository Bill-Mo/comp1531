from distance import longest_distance

def test_sample():
    assert(longest_distance([1,2,3,1,4]) == 3)
    assert(longest_distance([1,2,1,2,1]) == 4)
    assert(longest_distance([1,2,3,1,3]) == 3)

def test_zero():
    assert(longest_distance([1, 2, 3, 4, 5]) == 0)
