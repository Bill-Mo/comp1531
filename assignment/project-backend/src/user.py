import re
import uuid
import requests
import urllib.request
from flask import request as Flask_request
from flask import url_for
from io import BytesIO
from PIL import Image
from typing import Union
from datetime import datetime

import src.helper as helper 
from src.data import users, dms, channels
from src.auth import generate_token, new_session_id
from src.error import InputError
from src.channels import channels_list_v1
from src.dm import dm_list_v1

def convert_to_user_profile(auth_user_id: int) -> dict:
    '''
    Generates profile for user 
        
    Return Value:
        'user' - dictionary containing user profile 
    
    '''
    return {
        'u_id': auth_user_id,
        'email': users[auth_user_id]['email'],
        'name_first': users[auth_user_id]['name_first'],
        'name_last': users[auth_user_id]['name_last'],
        'handle_str': users[auth_user_id]['handle_str'],
    }
    
def users_all_v1(token: Union[str, bytes]) -> dict: 
    '''
    Reads a list of all users and associated profiles including u_id, first name,
    last name, email and hadle
    
    Arguments: 
        token <bytes> - unique user token

    Return Value:
        Returns a list of all users 
    
    '''
    
    helper.token_check(token)
    
    all_users = []
    for user in users:
        all_users.append(convert_to_user_profile(user))
    return {
        'users': all_users
    }
    
def user_profile_v2(token: Union[str, bytes], u_id: int) -> dict:
    '''
    For a valid user, this will return a user profile including user id, email, first name, last name and handle.
    
    Arguments: 
        token <bytes> - unique user token 
        u_id <int> - unique user id
        
    Exceptions:
        InputError - invalid user with u_id
    
    Return Value:
        Returns user profile 
    
    '''
    helper.token_check(token)
    helper.user_check(u_id)
    
    return {
        'user' : convert_to_user_profile(u_id)
    }


def user_profile_setname_v2(token: Union[str, bytes], name_first: str, name_last: str) -> dict:
    '''
    Updates the authorised user's first name and last name in profile
    
    Arguments: 
        token <bytes> - unique user token
        name_first <string> - user first name 
        name_last <string> - user last name 
    
    Exceptions:
        InputError - when name_first and name_last is not between 1 and 
                     50 characters 
    Return Value:
        Returns updated user profile
    
    '''
    token_decoded = helper.check_token(token)
    helper.token_check(token)
    
    
    if name_first is None or len(name_first)>50 or len(name_first)<1:
        raise InputError(description='Invalid name_first!')
        
    if name_last is None or len(name_last)>50 or len(name_last)<1:
        raise InputError(description='Invalid name_last!')
        
    users[token_decoded['auth_user_id']]['name_last'] = name_last
    users[token_decoded['auth_user_id']]['name_first'] = name_first
            
    return {}
    
        
def user_profile_setemail_v2(token: Union[str, bytes], email: str) -> dict:
    '''
    Updates the user email address
    
    Arguments: 
        token <bytes> - unique user token
        email <string> - user email
    
    Exceptions:
        InputError - when email entered is invalid
    
    Return Value:
        Returns new user email 
    
    '''
    token_decoded = helper.check_token(token)
    helper.token_check(token)
    
    email_regex = "^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$"
    
    if len(email) > 254:
        raise InputError(description='Invalid email address!')
    if email is None or not re.search(email_regex, email):
        raise InputError(description='Invalid email address!')
        
    for user in users: 
        if users[user]['email'] == email and user != token_decoded['auth_user_id']:
            raise InputError(description='Email address is already being used by another.')
    
    users[token_decoded['auth_user_id']]['email'] = email
    
    return {}

def user_profile_sethandle_v2(token: Union[str, bytes], handle_str: str) -> dict:
    '''
    Updates authorised user handle 
    
    Arguments: 
        token <bytes> - unique user token
        handle_str <string> - user handle 
    
    Exceptions:
        InputError - when handle_str is not between 3 and 20 characters or is
                     already being used by another user
    
    Return Value:
        returns user with updated handle 
    
    '''
    token_decoded = helper.check_token(token)
    helper.token_check(token)
    
    if handle_str is None or len(handle_str) < 3 or len(handle_str) > 20:
        raise InputError(description='Invalid length of handle_str!')
  
    # Check for existing handle_str
    for user in users: 
        if users[user]['handle_str'] == handle_str and user != token_decoded['auth_user_id']:
            raise InputError(description='Email address is already being used by another user.')        
    
    # Change handle
    users[token_decoded['auth_user_id']]['handle_str'] = handle_str
            
    return {}
    
def message_sent_list_v1(token, auth_user_id):
    '''
    checking for all messages sent by user
    '''
    user_channels = channels_list_v1(token)
    messages = []
    for channel_info in user_channels:
        for idx, msg_info in enumerate(channels[channel_info['channel_id']]['messages']):
            if channels[channel_info['channel_id']]['messages'][idx]['u_id'] == auth_user_id:
                messages.append(msg_info)
    user_dms = dm_list_v1(token)
    for dm_info in user_dms:
        for idx, msg_info in enumerate(dms[dm_info['dm_id']]['messages']):
            if dms[dm_info['dm_id']]['messages'][idx]['u_id'] == auth_user_id:
                messages.append(msg_info)
    return messages

def user_stats_v1(token):
    '''
    Returns a dictionary of user stats at given timestamp
    
    Arguments: 
        token <bytes> - unique user token
    
    Return Value:
        dictionary of user stats as per shape below
    '''
    
    token_decoded = helper.check_token(token)
    helper.token_check(token)

    time_stamp = int(datetime.now().timestamp())

    num_channels_joined = len(channels_list_v1(token))
    num_dms_joined = len(dm_list_v1(token))
    num_messages_sent = len(message_sent_list_v1(token, token_decoded['auth_user_id']))

    channels_joins = {'num_channels_joined': num_channels_joined, 'time_stamp': time_stamp}
    dms_joins = {'num_dms_joined': num_dms_joined, 'time_stamp': time_stamp}
    messages_sent = {'num_messages_sent': num_messages_sent, 'time_stamp': time_stamp}

    involvement_rate = (num_channels_joined + num_dms_joined + num_messages_sent) / (len(dms) + len(channels) + helper.num_messages_exist())

    return { 
        'user_stats' :{
            'channels_joined': [channels_joins],
            'dms_joined': [dms_joins],
            'messages_sent': [messages_sent],
            'involvement_rate' : involvement_rate
        }
    }

def users_stats_v1(token):
    '''
    Returns a dictionary of dream stats at given timestamp
    
    Arguments: 
        token <bytes> - unique user token
    
    Return Value:
        dictionary of dream stats as per shape below
    '''
    helper.token_check(token)
    time_stamp = int(datetime.now().timestamp())
    channels_exist = {'num_channels_exist': len(channels), 'time_stamp': time_stamp}
    dms_exist = {'num_dms_exist': len(dms), 'time_stamp': time_stamp}
    messages_exist = {'num_messages_exist': helper.num_messages_exist(), 'time_stamp': time_stamp}
    utilization_rate = helper.num_users_in_at_least_1_channel_or_dm()/len(users)
    return {
        'dreams_stats' :{
            'channels_exist': [channels_exist],
            'dms_exist': [dms_exist],
            'messages_exist': [messages_exist],
            'utilization_rate' : utilization_rate
        }
    }
    
def user_profile_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    '''
    Given URL of an image, crops the image within given bounds and uploads the photo to user profile 
    
    Arguments: 
        token <bytes> - unique user token
        img_url <string> - image url 
        x_start - width bounds
        y_start - height bounds
        x_end - width bounds
        y_end - height bounds
        
     Exceptions:
        InputError - when image url is not valid (http returns status other than 200, dimensions do not fit the image in the url or image type is not jpg/jpeg
    
    Return Value:
        returns user profile photo 
    
    '''
    token_decoded = helper.check_token(token)
    helper.token_check(token)

    file_name = str(token_decoded['auth_user_id']) + '.jpg'
    path_name = 'static/' + file_name
    
    #opening the image  
    try:
        pp = urllib.request.urlretrieve(img_url, path_name)
    except Exception as e:
        raise InputError(description="Image URL cannot be opened") from e
    
    pp = Image.open(path_name)

    #check if image is correct file type 
    if pp.format != 'JPEG':
        raise InputError(description="File type must be .jpg or .jpeg") 
    
    #checking image dimensions
    if x_start < 0 or y_start < 0:
        raise InputError(description="Incorrect dimensions")
        
    if x_end < x_start or y_end < y_start:
        raise InputError(description="Incorrect dimensions")
    
    #cropping image
    pp = pp.crop((x_start, y_start, x_end, y_end))
    pp.save(path_name)

    new_url = url_for('static', filename=file_name, _external=True)
    
    #updating profile photo in global variable 
    users[token_decoded['auth_user_id']]['profile_img_url'] = new_url
    
    return {}


    
