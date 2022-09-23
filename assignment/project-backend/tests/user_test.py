import pytest
from datetime import datetime
from src.user import convert_to_user_profile, users_all_v1, user_profile_v2, \
    user_profile_setname_v2, user_profile_setemail_v2, user_profile_sethandle_v2, \
    user_profile_uploadphoto, user_stats_v1, users_stats_v1
from src.auth import auth_register_v1, auth_login_v1
from src.channel import channel_join_v1
from src.channels import channels_create_v1
from src.dm import dm_create_v1
from src.message import message_send_v1
from src.error import InputError, AccessError
from src.other import clear_v1
from src.data import users, channels, dms

#function to create a user and log in
def generate_user():
    user = auth_register_v1("validEmail@email.com", "password", "Hayden", "James")   
    return user

#test for user profile 
def test_user_profile_v2():
    clear_v1()
    
    test_user = generate_user()
    
    profile = {
        'u_id': test_user['auth_user_id'],
        'email': "validEmail@email.com",
        'name_first': "Hayden",
        'name_last': "James",
        'handle_str': "haydenjames",
    }
    assert user_profile_v2(test_user['token'], test_user['auth_user_id']).get('user') == profile
    assert users_all_v1(test_user['token']) == {'users': [profile]}

#testing user set name
def test_user_profile_setname_v2():

    clear_v1()
    
    test_user = generate_user()
    
    user_profile_setname_v2(test_user['token'], "John", "Smith")
    profile = user_profile_v2(test_user['token'], test_user['auth_user_id']).get('user')
    
    assert profile['name_first'] == "John"
    assert profile['name_last'] == "Smith"

#test invalid input for first name is >50 characters
def test_user_profile_setname_v2_firstname_error():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_setname_v2(test_user['token'], "Chiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiicken", "Nug")

    
#test invalid input for first name if name is <1
def test_user_profile_setname_v2_firstname_error2():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_setname_v2(test_user['token'], "", "Nug")
    

#test invalid input for last name if name is >50 characters
def test_user_profile_setname_v2_lastname_error():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_setname_v2(test_user['token'],"Chicken", "Nuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuug")


#test invalid input for last name if name is <1 character
def test_user_profile_setname_v2_lastname_error2():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_setname_v2(test_user['token'], "Chicken", "")

    
#test user email function
def test_user_profile_setemail_v2():
    
    clear_v1()
    
    test_user = generate_user()
    
    user_profile_setemail_v2(test_user['token'], "testEmail@email.com")
    profile = user_profile_v2(test_user['token'], test_user['auth_user_id']).get('user')
    
    assert profile['email'] == "testEmail@email.com"

#test for invalid email input
def test_user_profile_setemail_v2_invalid():
    
    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_setemail_v2(test_user['token'], "invalid_incorrect_email@email.com")

#test for existing email error
def test_user_profile_setemail_v2_existingemail():
    
    clear_v1()
    
    test_user = generate_user()
    auth_register_v1("CheckEmail@email.com", "valid_password", "Chicken", "Nug")
    
    with pytest.raises(InputError):
        user_profile_setemail_v2(test_user['token'], "CheckEmail@email.com")
    with pytest.raises(InputError):
        user_profile_setemail_v2(test_user['token'], ("Apple" * 60) + "@email.com")

#test for set handle function
def test_user_profile_sethandle_v2():

    clear_v1()
    
    test_user = generate_user()
    
    user_profile_sethandle_v2(test_user['token'], "handler")
    profile = user_profile_v2(test_user['token'], test_user['auth_user_id']).get('user')
    
    assert profile['handle_str'] == "handler"

#test for existing handle error and invalid handle errors
def test_user_profile_sethandle_v2_existing():

    clear_v1()
    
    test_user = generate_user()
    
    user_profile_sethandle_v2(test_user['token'], "HANDLEBAR")
    
    existing_user = auth_register_v1("NewEmail@email.com", "valid_password", "Chicken", "Nug")

    with pytest.raises(InputError):
        user_profile_sethandle_v2(existing_user['token'], "HANDLEBAR")
    with pytest.raises(InputError):
        user_profile_sethandle_v2(existing_user['token'], "")
    with pytest.raises(InputError):
        user_profile_sethandle_v2(existing_user['token'], "A")
    with pytest.raises(InputError):
        user_profile_sethandle_v2(existing_user['token'], "HANDLEBARHANDLEBARHANDLEBAR")
    
def test_single_user():

    clear_v1()
    
    test_user = generate_user()

    user_profile_sethandle_v2(test_user['token'], "haydenjames")

    clear_v1()

#test for input error
def test_user_profile_uploadphoto_input_error():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_uploadphoto(test_user['token'], 'https://i.imgr.com/wtNb5NL.jpg', 0, 0, 200, 200)
        
#test for incorrect dimension
def test_user_profile_uploadphoto_incorrect_dimension():

    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_uploadphoto(test_user['token'], 'https://i.imgur.com/wtNb5NL.jpg', 1700, 1700, 800, 800)
        
#test for incorrect file type
def test_user_profile_uploadphoto_incorrect_file():
    
    clear_v1()
    
    test_user = generate_user()
    
    with pytest.raises(InputError):
        user_profile_uploadphoto(test_user['token'], 'https://i.imgur.com/170hfv9.png', 0, 0, 200, 200)

#test for user stats v1
def test_user_stats_v1():

    clear_v1()
  
    test_user1 = auth_register_v1("apple@email.com", "valid_password1", "Chicken", "Nug")
    test_user2 = auth_register_v1("banana@email.com", "valid_password2", "Mc", "Donalds")
    channel_id = channels_create_v1(test_user1['token'], 'channel', True)
    dm = dm_create_v1(test_user1['token'], [test_user2['auth_user_id']])
    message_send_v1(test_user1['token'], channel_id, 'Hello', True)
    message_send_v1(test_user1['token'], dm['dm_id'], 'Goodbye', False)

    time_now = int(datetime.now().timestamp())
    answer = {
        'channels_joined': [{'num_channels_joined': 1, 'time_stamp': time_now}],
        'dms_joined': [{'num_dms_joined': 1, 'time_stamp': time_now}],
        'messages_sent': [{'num_messages_sent': 2, 'time_stamp': time_now}],
        'involvement_rate' : 1
    }

    assert user_stats_v1(test_user1['token']).get('user_stats') == answer

def test_user_stats_v1_existing_messages():

    clear_v1()
  
    test_user1 = auth_register_v1("apple@email.com", "valid_password1", "Chicken", "Nug")
    test_user2 = auth_register_v1("banana@email.com", "valid_password2", "Mc", "Donalds")
    channel_id = channels_create_v1(test_user1['token'], 'channel', True)
    channel_join_v1(test_user2['token'], channel_id)
    dm = dm_create_v1(test_user1['token'], [test_user2['auth_user_id']])
    message_send_v1(test_user2['token'], channel_id, 'Hello', True)
    message_send_v1(test_user2['token'], dm['dm_id'], 'Goodbye', False)

    time_now = int(datetime.now().timestamp())
    answer = {
        'channels_joined': [{'num_channels_joined': 1, 'time_stamp': time_now}],
        'dms_joined': [{'num_dms_joined': 1, 'time_stamp': time_now}],
        'messages_sent': [{'num_messages_sent': 0, 'time_stamp': time_now}],
        'involvement_rate' : 0.5
    }

    assert user_stats_v1(test_user1['token']).get('user_stats') == answer

#test for users stats v1
def test_users_stats_v1():

    clear_v1()
    
    test_user1 = auth_register_v1("apple@email.com", "valid_password1", "Chicken", "Nug")
    test_user2 = auth_register_v1("banana@email.com", "valid_password2", "Mc", "Donalds")
    channel_id = channels_create_v1(test_user1['token'], 'channel', True)
    dm = dm_create_v1(test_user1['token'], [test_user2['auth_user_id']])
    message_send_v1(test_user1['token'], channel_id, 'Hello', True)
    message_send_v1(test_user1['token'], dm['dm_id'], 'Goodbye', False)
    
    time_now = int(datetime.now().timestamp())
    answer = {
        'channels_exist': [{'num_channels_exist': 1, 'time_stamp': time_now}],
        'dms_exist': [{'num_dms_exist': 1, 'time_stamp': time_now}],
        'messages_exist': [{'num_messages_exist': 2, 'time_stamp': time_now}],
        'utilization_rate' : 1
    }

    assert users_stats_v1(test_user1['token']).get('dreams_stats') == answer

#test for users stats v1
def test_users_stats_lone_user():

    clear_v1()
    
    test_user1 = auth_register_v1("apple@email.com", "valid_password1", "Chicken", "Nug")
    auth_register_v1("banana@email.com", "valid_password2", "Mc", "Donalds")
    channel_id = channels_create_v1(test_user1['token'], 'channel', True)
    dm = dm_create_v1(test_user1['token'], [])
    message_send_v1(test_user1['token'], channel_id, 'Hello', True)
    message_send_v1(test_user1['token'], dm['dm_id'], 'Goodbye', False)
    
    time_now = int(datetime.now().timestamp())
    answer = {
        'channels_exist': [{'num_channels_exist': 1, 'time_stamp': time_now}],
        'dms_exist': [{'num_dms_exist': 1, 'time_stamp': time_now}],
        'messages_exist': [{'num_messages_exist': 2, 'time_stamp': time_now}],
        'utilization_rate' : 0.5
    }

    assert users_stats_v1(test_user1['token']).get('dreams_stats') == answer

@pytest.mark.skip
def test_upload_photo():
    clear_v1()
    
    test_user = generate_user()
    
    assert user_profile_uploadphoto(test_user['token'], 'https://ibb.co/W6jV21B', 0, 0, 800, 800) == {}