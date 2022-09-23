from flask import Flask, request
import datetime
from json import dumps

APP = Flask(__name__)

@APP.route('/getcount', methods=['GET'])
def count():
    tag = request.args.get('tag')
    return dumps(name)

if __name__ == "__main__":
    APP.run(port=8080)
