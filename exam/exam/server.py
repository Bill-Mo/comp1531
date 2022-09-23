'''
The flask server wrapper

All endpoints return JSON as output.
All POST requests pass parameters through JSON instead of Form.
'''
from json import dumps
from flask import Flask, request

import brooms

APP = Flask(__name__)

'''
Endpoint: '/users'
Method: GET
Parameters: ()
Output: { "users": [ ... list of strings ... ] }

Returns a list of all the users as a list of strings.
'''
# Write this endpoint here
@APP.route('/users', methods=['GET'])
def get_u():
    return dumps(get_users())


'''
Endpoint: '/users'
Method: POST
Parameters: ( name: string )
Output: {}

Adds a user to the room/broom.
'''
# Write the endpoint here
@APP.route('/users', methods=['POST'])
def add_u():
    incoming = request.get_json()
    add_user(incoming['name'])
    return dumps({})

'''
Endpoint: '/message'
Method: GET
Parameters: ()
Output: { "messages": [ { "from" : string, "to" : string, "message" : string } ] }

Returns a list of all the messages sent, who they came from, and who they are going to.
'''
# Write the endpoint here
@APP.route('/message', methods=['GET'])
def get_m():
    return dumps(get_messages())

'''
Endpoint: '/message'
Method: POST
Parameters: (user_from: string, user_to: string, message: string)
Output: {}

Sends a message from user "user_from" to user "user_to". All three parameters are strings.
'''
# Write the endpoint here
@APP.route('/message', methods=['POST'])
def send_m():
    incoming = request.get_json()
    send_message(incoming['user_from'], incoming['user_to'], incoming['message'])
    return dumps({})

if __name__ == '__main__':
    APP.run(debug=True, port = 8080)
