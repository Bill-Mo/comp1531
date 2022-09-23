import pytest
import json

from src.auth import auth_register_v1, auth_passwordreset_request_v1, \
                    auth_passwordreset_reset_v1, password_encode
from src.error import InputError, AccessError
from src.other import clear_v1
from src.data import users
import src.helper as helper

'''
These tests will test the functionality of of the auth_password_reset_v1 and 
auth_passwordreset_reset_v1

    User 1 is Dreams Owner
    User 2 is member of Dreams 

'''

def test_password_reset_valid_owner():
    '''
    This test checks that a valid password reset can be performed by the owner of Dreams
    '''
    clear_v1()

    # Valid information has been summitted to register from the first user/Dreams Owner
    user1 = auth_register_v1('apple@gmail.com', 'password1', 'Steve', 'Jobs')
    # Vadid information has been summitted to register from the second user (not Dreams owner)
    auth_register_v1('banana@com.au', 'password2', 'Steven', 'Jacobs')
    
    # Dreams Owner send a password reset request
    assert auth_passwordreset_request_v1("apple@gmail.com") == {}

    # Dreams Owner change the password
    assert auth_passwordreset_reset_v1(users[user1['auth_user_id']]['reset_code'][0], "X3e$rfv") == {}

    assert users[user1['auth_user_id']]['password'] == password_encode("X3e$rfv")

def test_password_reset_invalid_user():
    clear_v1()
    with pytest.raises(InputError):
        auth_passwordreset_request_v1("someRandomEmail@gmail.com")

def test_password_reset_valid_member():
    '''
    This test checks that a valid password reset can be performed by the member of Dreams
    '''
    clear_v1()

    # Valid information has been summitted to register from the first user/Dreams Owner
    auth_register_v1('apple@gmail.com', 'password1', 'Steve', 'Jobs')
    # Vadid information has been summitted to register from the second user (not Dreams owner)
    user2 = auth_register_v1('banana@com.au', 'password2', 'Steven', 'Jacobs')
    
    # User 2 send a password reset request
    assert auth_passwordreset_request_v1("banana@com.au") == {}

    # User 2 change the password
    assert auth_passwordreset_reset_v1(users[user2['auth_user_id']]['reset_code'][0], "X3e$rfv") == {}

    assert users[user2['auth_user_id']]['password'] == password_encode("X3e$rfv")
  

def test_password_reset_invalid_reset_code():
    '''
    This test checks that reset_code that is not a valid reset code will lead to InputError
    '''
    clear_v1()

    # Valid information has been summitted to register from the first user/Dreams Owner
    auth_register_v1('apple@gmail.com', 'password1', 'Steve', 'Jobs')
    # Vadid information has been summitted to register from the second user (not Dreams owner)
    auth_register_v1('banana@com.au', 'password2', 'Steven', 'Jacobs')
    
    # User 2 send a password reset request
    assert auth_passwordreset_request_v1("banana@com.au") == {}

    # User 2 change the password with reset_code that has only 3 digits
    with pytest.raises(InputError):
        auth_passwordreset_reset_v1(str(123), "Queen47")
    # Reset code does not exist in any user's reset code list
    with pytest.raises(InputError):
        auth_passwordreset_reset_v1(str(9999), "Queen47")



def test_new_password_reset():
    '''
    This test checks that new password that is not a valid will lead to InputError
    '''
    clear_v1()

    # Valid information has been summitted to register from the first user/Dreams Owner
    auth_register_v1('apple@gmail.com', 'password1', 'Steve', 'Jobs')
    # Vadid information has been summitted to register from the second user (not Dreams owner)
    user2 = auth_register_v1('banana@com.au', 'password2', 'Steven', 'Jacobs')
    
    # User 2 send a password reset request
    assert auth_passwordreset_request_v1("banana@com.au") == {}

    # User 2 change the password with insufficient new password
    reset_code = users[user2['auth_user_id']]['reset_code'][0]
    with pytest.raises(InputError):
        auth_passwordreset_reset_v1(reset_code, "Q67")

