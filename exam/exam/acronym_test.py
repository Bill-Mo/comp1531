from acronym import acronym_make
import pytest

def test_1():
    assert acronym_make(['I am very tired today']) == ['VTT']
    assert acronym_make(['Why didnt I study for this exam more', 'I dont know']) == ['WDSFTM', 'DK']
    assert acronym_make(['what Is your Name']) == ['WYN']
    
def test_long():
    assert acronym_make(['s s s s s s s s s s s s s s s s']) == ['N/A']

def test_vowel():
    assert acronym_make(['a e i o u']) == []
    assert acronym_make(['and ege is October us']) == []
    
def test_empty():
    with pytest.raises(ValueError):
        acronym_make([])
