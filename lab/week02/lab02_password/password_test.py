'''
Tests for check_password()
'''
from password import check_password

def test_password():
    assert(check_password('123456')) == 'Horrible password'
    
    assert(check_password('asfs1A')) == 'Poor password'
    
    assert(check_password('afasfasfasLGGV52')) == 'Strong password'
    
    assert(check_password('sssssss1')) == 'Moderate password'
    
    assert(check_password(123456789101112)) == 'Moderate password'
