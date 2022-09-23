import pytest
import requests
import json
from src import config
from src.data import users 




def test_password_reset_invalid():
    '''
    Testing server functionality of auth_passwordreset_request and auth_passwordreset_reset
    This will test invalid reset code provided by the owner of Dreams - user 1
    '''

    clear = requests.delete(config.url + 'clear/v1')
    assert clear.status_code == 200


    # Valid information has been summitted to register from the first user// Dreams Owner
    u1 = requests.post(config.url + "auth/register/v2", json={
        'email': "apple@gmail.com",
        'password': "Lhgi00d",
        'name_first': "Lil",
        'name_last': "Wayne"
    })
    assert u1.status_code == 200
    
    # Valid information has been summitted to register from the second user//Dreams member 
    u2 = requests.post(config.url + "auth/register/v2", json={
        'email': "iamhappy@unsw.org",
        'password': "VuulkanFs",
        'name_first': "Bill",
        'name_last': "Shorten"
    })
    assert u2.status_code == 200

    # User1 send a password reset request
    passreset1 = requests.post(config.url + "/auth/passwordreset/request/v1", json={
        'email': "apple@gmail.com",
    })
    assert passreset1.status_code == 200
    
    # User1 change the password with invalid reset code
    invalidcode1 = requests.post(config.url + "/auth/passwordreset/reset/v1", json={
        'reset_code': 123,
        'new_password': "1q2w3w",
    })
    assert invalidcode1.status_code == 400