import pytest
import requests
import json
from src import config

@pytest.fixture
def setup():
    clear = requests.delete(config.url + 'clear/v1')
    assert clear.status_code == 200

    # Create User 1 - Dreams Owner
    u1_payload = requests.post(config.url + "auth/register/v2", json={
        'email': 'apple@com.au', 
        'password': 'password1', 
        'name_first': 'Steve', 
        'name_last': 'Jobs'
    })
    assert u1_payload.status_code == 200
    u1_payload = u1_payload.json()

    return {
        'user' : u1_payload
    }

def test_user_profile_setname_v2(setup):
    setname = requests.put(config.url + 'user/profile/setname/v2', json={
        'token': setup['user']['token'], 
        'name_first': 'Hayden', 
        'name_last': 'Jacobs'
    })
    assert setname.status_code == 200
    resp = requests.get(config.url + 'user/profile/v2', params={
        'token': setup['user']['token'], 
        'u_id': setup['user']['auth_user_id']
    })
    assert resp.status_code == 200
    profile = resp.json().get('user')
    assert profile['name_first'] == 'Hayden'
    assert profile['name_last'] == 'Jacobs'
    
def test_user_profile_setemail_v2(setup):
    setname = requests.put(config.url + 'user/profile/setemail/v2', json={
        'token': setup['user']['token'], 
        'email': 'cs1531@com.au'
    })
    assert setname.status_code == 200
    resp = requests.get(config.url + 'user/profile/v2', params={
        'token': setup['user']['token'], 
        'u_id': setup['user']['auth_user_id']
    })
    assert resp.status_code == 200
    profile = resp.json().get('user')
    assert profile['u_id'] == setup['user']['auth_user_id']
    assert profile['email'] == 'cs1531@com.au'
    
def test_user_profile_sethandle_v1(setup):
    setname = requests.put(config.url + 'user/profile/sethandle/v1', json={
        'token': setup['user']['token'], 
        'handle_str': 'haydenjacobs'
    })
    assert setname.status_code == 200
    resp = requests.get(config.url + 'user/profile/v2', params={
        'token': setup['user']['token'], 
        'u_id': setup['user']['auth_user_id']
    })
    assert resp.status_code == 200
    profile = resp.json().get('user')
    assert profile['u_id'] == setup['user']['auth_user_id']
    assert profile['handle_str'] == 'haydenjacobs'
    
def test_users_all_v1(setup):
    resp = requests.get(config.url + '/users/all/v1', params={
        'token': setup['user']['token']
    })
    assert resp.status_code == 200
    profile = resp.json().get('users')
    assert len(profile) == 1

def test_user_profile_uploadphoto_invalidurl(setup):
    setname = requests.post(config.url + 'user/profile/uploadphoto/v1', json={
        'token': setup['user']['token'],
        'img_url': 'https://imgur.com/invalidurl',
        'x_start': 0,
        'y_start': 0,
        'x_end': 200,
        'y_end': 200
    })
    
    assert setname.status_code == 400

def test_user_profile_uploadphoto_invalidfile(setup):
    setname = requests.post(config.url + 'user/profile/uploadphoto/v1', json={
        'token': setup['user']['token'],
        'img_url': 'https://i.imgur.com/170hfv9.png',
        'x_start': 0,
        'y_start': 0,
        'x_end': 200,
        'y_end': 200
    })

    assert setname.status_code == 400

def test_user_profile_uploadphoto_invaliddimension(setup):
    setname = requests.post(config.url + 'user/profile/uploadphoto/v1', json={
        'token': setup['user']['token'], 
        'img_url': 'https://i.imgur.com/wtNb5NL.jpg',
        'x_start': 1800,
        'y_start': 1800,
        'x_end': 900,
        'y_end': 900
    })

    assert setname.status_code == 400

@pytest.mark.skip
def test_upload_photo(setup):
    setname = requests.post(config.url + 'user/profile/uploadphoto/v1', json={
        'token': setup['user']['token'], 
        'img_url': 'https://cdn.pixabay.com/photo/2017/09/25/13/12/dog-2785074__340.jpg',
        'x_start': 0,
        'y_start': 0,
        'x_end': 400,
        'y_end': 400
    })
    assert setname.status_code == 200
    
    resp = requests.get(config.url + 'user/profile/v2', params={
        'token': setup['user']['token'], 
        'u_id': setup['user']['auth_user_id']
    })
    assert resp.status_code == 200
    profile = resp.json().get('user')
    u_id = setup['user']['auth_user_id']

    assert profile == {
                    'u_id': u_id,
                    'email': "apple@com.au",
                    'name_first': "Steve",
                    'name_last': "Jobs",
                    'handle_str': "stevejobs",
                    'profile_img_url': f'{config.url}static/{u_id}.jpg',
                }