from list_exercises import *

def test_reverse():
    l = ["how", "are", "you"]
    reverse_list(l)
    assert l == ["you", "are", "how"]
    
    reverse_list(l)
    assert l == ["how", "are", "you"]
    
    numl = [1, 2, 3]
    reverse_list(numl)
    assert numl == [3, 2, 1]

def test_min_positive():
    assert minimum([1, 2, 3, 10]) == 1
    
    assert minimum([2, 2, 2]) == 2
    
    assert minimum([-3, 0, 2]) == -3

def test_sum_positive():
    assert sum_list([7, 7, 7]) == 21
    
    assert sum_list([-3, -2, -1]) == -6
    
    assert sum_list([1233, 5251, 2746]) == 9230
