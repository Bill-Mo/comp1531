import re
import jwt
import json
import uuid
import hashlib
from typing import Optional, NoReturn, Union
from src.error import InputError
from src.data import users
import src.helper as helper
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#secret for token
SECRET = 'This is a very safe secret'

def auth_register_v1(email: str, password: str, name_first: str, name_last: str) -> dict:
    '''
    Given a user's first and last name, email address, and password, 
    create a new account for them
    
    Arguments: 
        email <str> - email of users
        password <str> - password of users
        name_first <str> - first name of users
        name_last <str> - last name of users
    
    Exceptions:
        InputError:
            Email entered is not a valid email using the method provided here (unless you feel you have a better method).
            Email address is already being used by another user
            Password entered is less than 6 characters long
            name_first is not between 1 and 50 characters inclusively in length
            name_last is not between 1 and 50 characters inclusively in length
    
    Return value:
        return a new 'token' for that session and user id
    '''

    #Email entered is not a valid email
    if re.search('^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$', email) == None:
        raise InputError(description='Invalid email')
        
    #Email address is already being used by another
    email_exists = False 
    if len(users) > 0:
        for user in users: 
            if users[user]['email'] == email:
                email_exists = True
    if email_exists is True:
        raise InputError(description='Email address is already being used by another')

    #Password entered is less than 6 characters long
    if len(password) < 6:
        raise InputError(description='Password is too short.')

    #name_first is not between 1 and 50 characters inclusively in length
    if not (1 <= len(name_first) <= 50):
        raise InputError(description='First name is too short or too long')
        
    #name_last is not between 1 and 50 characters inclusively in length
    if not (1 <= len(name_last) <= 50):        
        raise InputError(description='Last name is too short or too long')

    #generate a handle
    handle = make_handle(name_first, name_last)

    #return user id
    u_id = len(users) + 1
    
    users[u_id] = {
        'session_id': [],
        'permission_id': 2,
        'email' : email,
        'password' : hashlib.sha256(password.encode()).hexdigest(),
        'name_first' : name_first,
        'name_last' : name_last,
        'handle_str': handle,
        'notifications' : [],
        'profile_img_url': [],
        'reset_code' : [],
    }

    if u_id == 1:
        users[u_id]['permission_id'] = 1         

    #return a new token
    s_id = new_session_id()
    users[u_id]['session_id'].append(s_id)
    token = generate_token(s_id)
    return {'token': token, 'auth_user_id': u_id}

def auth_login_v1(email: str, password: str) -> dict:
    '''
    Given a registered users' email and password and returns a new 
    `token` for that session
    
    Arguments:
        email <str> - email of users
        password <str> - password of users
    
    Exceptions:
        InputError:
            Email entered is not a valid email
            Email entered does not belong to a user
            Password is not correct
            
    Return value:
        return a new 'token' for that session and user id
    '''

    #Email entered is not a valid email
    if re.search('^[a-zA-Z0-9]+[\\._]?[a-zA-Z0-9]+[@]\\w+[.]\\w{2,3}$', email) == None:
        raise InputError(description='Invalid email.')

    #Email entered does not belong to a user 
    email_exists = False 
    for user in users: 
        if users[user]['email'] == email:
            u_id = user
            email_exists = True
    if email_exists is False:
        raise InputError('Email does not belong to a user.')

    #Password is not correct
    if hashlib.sha256(password.encode()).hexdigest() != users[u_id]['password']:
        raise InputError(description='Incorrect password. Please try again.')
        
    #Return auth_user_id and a new token
    s_id = new_session_id()
    users[u_id]['session_id'].append(s_id)
    token = generate_token(s_id)
    return {'token': token, 'auth_user_id': u_id}

def auth_logout_v1(token: Union[str, bytes]) -> dict:
    '''
    Given an active token, invalidates the token to log the user out. 
    If a valid token is given, and the user is successfully logged 
    out, it returns true, otherwise false.
    
    Arguments:
        email <str> - email of users
        password <str> - password of users
    
    Exceptions: N/A
            
    Return value:
        if users are logout successfully, return true. Otherwise, 
        return false.
    '''

    #Token passed is valid or not
    helper.token_check(token)

    #Given an active token, invalidates the token to log the user out.
    decode = jwt.decode(token, SECRET, algorithms = ['HS256'])
    s_id = decode['session_id']
    global users
    for user in users:
        for status in users[user]['session_id']:
            if status == s_id:
                users[user]['session_id'].remove(s_id)
                return {'is_success': True}
    return {'is_success': False}



def auth_passwordreset_request_v1(email :str) -> dict:
    '''
    Given an email address, if the user is a registered user, sends them an email
    containing a specific secret code, that when entered in auth_passwordreset_reset,
    shows that the user trying to reset the password is the one who got sent this email.

    Arguments:
        email <string> - unique user email

    Exceptions:
        InputError  - Occurs when email is not valid (Assumption)

    Return Value:
        dict: void dict
    

    '''
    #create a random combination of a 4 digit reset code
    sample_numbers = '1234567890'
    reset_code = ''.join((random.choice(sample_numbers) for i in range(4)))

    #search if registered user has an email
    user = email_search(email)

    if (user == None):
        raise InputError(description='Invalid Email: Email is not registered')

    #add reset code to user dict -->making it valid for user
    users[user]['reset_code'].append(reset_code)

    #send an  email containing reset code to user's emsil
    send_email(email, reset_code)

    return {}

def auth_passwordreset_reset_v1(reset_code :str, new_password :str) -> dict:

    '''
    Given a reset code for a user, set that user's new password 
    to the password provided

    Arguments:
        email <string> - unique user email
        new_password <string> - unique new password that is 6 characters long

    Exceptions:
        InputError  - Occurs when reset_code is not a valid reset code
                    - Password entered is less than 6 characters long

    Return Value:
        dict: void dict
    
    '''
    #check authenticity of the reset code
    u_id = check_reset_code(reset_code)

    #check new password is valid
    check_valid_password(new_password)

    #change user's password to new password
    password_change(u_id, password_encode(new_password))

    return {}


### 
# The following functions below are helper functions that are specific to auth.py 
###
### Helper Functions ###

def generate_token(s_id: str) -> Union[str, bytes]:
    '''
    This helper function will generate a token
    '''
    return jwt.encode({'session_id': s_id}, SECRET, algorithm = 'HS256')

def new_session_id() -> str:
    '''
    This helper function will get a new session_id
    '''
    return str(uuid.uuid1())

def make_handle(name_first: str, name_last: str) -> str:
    '''
    This helper function will make a user handle using their first and last names
    '''
    concat = name_first + name_last
    concat = concat.lower()
    if len(concat) > 20:
        concat = concat[:20]
    copy_concat = concat
    append_number = 0
    while True:
        for user in users:
            if users[user]['handle_str'] == copy_concat:
                copy_concat = concat + str(append_number)
                append_number += 1
                continue
        return copy_concat

def email_search(email: str) -> Optional[int]:
    '''
    This helper function will Loop through the database to find whether there is a same email in the database
    '''
    for user in users:
        if users[user]['email'] == email:
            return user
    return None

def reset_code_check(reset_code: str) -> Optional[int]:
    '''
    This helper function will verify the authenticity of the user with reset code
    '''
    for user in users:
        if reset_code in users[user]['reset_code']:
            return user
    return None

def check_reset_code(reset_code: str) -> Union[NoReturn, int]:
    '''
    This helper function will verify the authenticity of the reset code
    '''
    u_id = reset_code_check(reset_code)
    if u_id == None:
        raise InputError(description="reset_code is not a valid reset code")
    return u_id

def check_valid_password(password: str):
    '''
    This helper function will verify the authenticity of password
    '''
    if len(password) in range(0, 6):
        raise InputError(description="Password entered is less than 6 characters long")

def password_encode(password: str) -> str:
    ''' 
    This helper function will Return the encoded password
    '''
    return hashlib.sha256(password.encode()).hexdigest()    

def password_change(u_id: int, new_password: str):
    ''' 
    This helper function will ccreate a new password
    '''
    users[u_id]['password'] = new_password

def send_email(email: str, reset_code: str):
    ''' 
    This helper function is responsible for sending the email containing reset code
    '''
    sender = "dreams.w13cdorito@gmail.com"
    recepient = f"""{email}"""

    # Create message container.
    msg = MIMEMultipart()
    msg['Subject'] = "Reset your Dreams Password"
    msg['From'] = sender
    msg['To'] = recepient

    # Create the body of the message.
    text = ""
    html = f"""\
    <html>
    <head></head>
    <body>
        <p>Hello,<br>
        <br>
        We wanted to let you know that you requested to reset your password.<br>
        <br>
        Your four digit reset pin is: {reset_code}.<br>
        <br>
        If you don't wish to reset your password, disregard this email.<br>
        <br>
        Kind Regards. The Wednesday 13C Doritos Dreams Team.<br>
        </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    # mail.ehlo()
    mail.starttls()
    mail.login('dreams.w13cdorito@gmail.com', 'RudraKaiqi13')
    mail.sendmail(sender, recepient, msg.as_string())
    mail.quit()

