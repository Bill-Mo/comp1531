import jwt
from time import time
from datetime import datetime
from src.data import users, channels, dms
from src.error import InputError, AccessError
from typing import Union, Optional

#secret for token
SECRET = 'This is a very safe secret'

def check_token(token: Union[str, bytes]) -> dict:
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        session_id = payload['session_id'] 
        status = True
        for user in users:
            if session_id in users[user]['session_id']:
                return {'status' : status, 'auth_user_id' : user}
        user = None
    except jwt.InvalidSignatureError:
        status = False
    return {'status' : status, 'auth_user_id' : None}

def token_check(token: Union[str, bytes]) -> None:
    '''
    Checks for valid token
    '''
    token_decoded = check_token(token)
    if token_decoded['status'] is False or token_decoded['auth_user_id'] is None:
        raise AccessError(description='Invalid Token: Token does not exist')

def user_check(auth_user_id: int) -> bool:
    '''
    Checks for valid auth_user_id
    '''
    for user in users:
        if int(auth_user_id) == user:
            return True
    raise InputError(description='Invalid User: User does not exist')

def channel_check(channel_id: int) -> None:
    '''
    Checks if channel exists
    '''
    if channel_id not in channels: 
        raise InputError(description='Invalid Channel: Channel does not exist')

def dm_check(dm_id: int) -> None:
    '''
    Checks if dm exists
    '''
    if dm_id not in dms: 
        raise InputError(description='Invalid DM: DM does not exist')

def user_in_channel_check(auth_user_id: int, channel_id: int) -> None:
    '''
    Checks if user is in channel
    '''
    info = user_info(auth_user_id)
    if info not in channels[channel_id]['all_members']:
        raise AccessError(description='Invalid User: User is not in channel list')

def user_in_dm_check(auth_user_id: int, dm_id: int) -> None:
    '''
    Checks if user is in dm
    '''
    if auth_user_id != dms[dm_id]['owner'] and auth_user_id not in dms[dm_id]['members']:
        raise AccessError(description='Invalid User: User is not in dm list')

def user_own_dm_check(auth_user_id: int, dm_id: int) -> None:
    '''
    Checks if user is the creator of dm
    '''
    if auth_user_id != dms[dm_id]['owner']:
        raise AccessError(description='Invalid User: User is not the owner')

def user_info(auth_user_id: int) -> dict:
    return {
        'u_id': auth_user_id,
        'email': users[auth_user_id]['email'],
        'name_first': users[auth_user_id]['name_first'],
        'name_last': users[auth_user_id]['name_last'],
        'handle_str': users[auth_user_id]['handle_str'],
        'profile_img_url': users[auth_user_id]['profile_img_url'], 
    }

def channel_info(channel_id: int) -> dict:
    return {
        'channel_id': channel_id,
        'name': channels[channel_id]['name']
    }

def check_handle(handle: str) -> Optional[int]:
    for user in users:
        if users[user]['handle_str'] == handle:
            return user
    return None

def user_own_channel_check(auth_user_id: int, channel_id: int) -> None:
    '''
    Checks if user is the owner of channel
    '''
    if user_info(auth_user_id) not in channels[channel_id]['owner_members']:
        raise AccessError(description='Invalid User: User is not the owner')

def uniqid() -> int:
    x=time()*10000000
    return int(x)
    
def channels_include_user(auth_user_id: int) -> list:
    '''
    checking for which channels the user is included in 
    '''
    user_channels = []
    info = user_info(auth_user_id)
    for channel_id in channels:
        if info in channels[channel_id]['all_members']:
            user_channels.append(channel_id)
    return user_channels 

def dms_include_user(auth_user_id: int) -> list:
    '''
    checking for user in all dms 
    '''
    user_dms = []
    for dm_id in dms:
        if auth_user_id == dms[dm_id]['owner'] or auth_user_id in dms[dm_id]['members']:
            user_dms.append(dm_id)
    return user_dms 
            
def num_users_in_at_least_1_channel_or_dm() -> int:
    '''
    list of users in at least 1 channel or dm
    '''
    num_users = 0
    for auth_user_id in users:
        if len(channels_include_user(auth_user_id)) > 0 or len(dms_include_user(auth_user_id)) > 0: 
            num_users += 1
    return num_users

def num_messages_exist() -> int:
    '''
    counting all existing messages sent 
    '''
    total_messages = 0
    for channel_id in channels:
        total_messages += len(channels[channel_id]['messages'])
    for dm_id in dms:
        total_messages += len(dms[dm_id]['messages'])
    return total_messages
    
