from count import count_char

def test_empty():
    assert count_char("") == {}

def test_simple():
    assert count_char("abc") == {"a": 1, "b": 1, "c": 1}

def test_double():
    assert count_char("aa") == {"a": 2}
    
def test_all():
    assert count_char('abcdefghijklmnopqrstuvwxyz') == {'a': 1, 'b': 1, 'c':1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i':1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o':1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u':1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    
def test_multiple():
    assert count_char('ffffffffffffffffffffqqqqqqqqqqqqqq') == {'f': 20, 'q': 14}
    
def test_not_letter():
    assert count_char('..;/ [])*(&*^$%') == {'.': 2, ';': 1, '/': 1, ' ': 1, '[': 1, ']': 1, ')': 1, '*': 2, '(': 1, '&': 1, '^': 1, '$': 1, '%': 1}
