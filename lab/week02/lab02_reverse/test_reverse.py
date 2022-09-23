'''
Tests for reverse_words()
'''
from reverse import reverse_words

def test_example():
    assert reverse_words(["Hello World", "I am here"]) == ['World Hello', 'here am I']
    
    assert reverse_words(['']) == ['']
    
    assert reverse_words(['1 2 3 4 5', '6 7 8 9']) == ['5 4 3 2 1', '9 8 7 6']
    assert reverse_words(['This is a very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very long string']) == ['string long very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very very a is This']
    
    assert reverse_words(['test test test']) == ['test test test']
    
    assert reverse_words(['Dog and cat, which one do you like best?']) == ['best? like you do one which cat, and Dog']
