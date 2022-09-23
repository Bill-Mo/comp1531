'''
The backend for a messaging system between users in a virtual room.

This system works based on a single room that users can be added to. Once a user
is added to the room, they are able to message any other user who has been added
to the room before. The details of the users and details of the messages can be
read at any time. Users are identified simply via a string, where each unique ASCII
string denotes a user (no need to create unique numeric IDs etc)
'''

# Put any global variables your implementation needs here
users = []
messages = []

def get_users():
    '''
    Returns a dictionary, whose sole key "users", contains a list of all the users.

    E.G. {"users":["Hayden", "Rob", "Emily", "Bart"]}

    The list is in reverse order in which they were added. So the
    first element of the list is the most recently added user.
    '''
    reverse = users
    reverse.reverse()
    return {'users': reverse}

def add_user(name):
    '''
    Adds a user to the room/broom.

    This function returns an empty dictionary.

    If a user with the same name is already in the room, it raises a KeyError
    '''
    global users
    if name in users:
        raise KeyError()
    users.append(name)
    return {}

def get_messages():
    '''
    Returns a dictionary, whose sole key "messages", contains a list of all the messages sent, who they came from,
    and who they are going to. The format of the return can be seen in brooms_test.py.

    The messages are listed in the order in which they were added. I.E. The first message
    in the list is the oldest message that was sent.
    '''
    return {'messages': messages}

def send_message(user_from, user_to, message):
    '''
    Sends a message from user "user_from" to user "user_to". All three parameters
    are strings.

    In reality the notion of what sending a message means is not something you have
    to over-think here. You're simply trying to capture information and store it for
    the get_messages function to work correctly.

    This function returns an empty dictionary.

    If either user_from or user_to are not in the room, it raises a KeyError.
    '''
    if user_from not in users or user_to not in users:
        raise KeyError()
    message = {
        'from': user_from, 
        'to': user_to, 
        'message': message, 
    }
    messages.append(message)
    return {}

def clear():
    '''
    Removes all data from the room/broom.

    Returns an empty dictionary.
    '''
    global users, messages
    users= []
    messages = []
    return {}
