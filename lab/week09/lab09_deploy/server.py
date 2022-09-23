from flask import Flask, request
from json import dumps
from number_fun import multiply_by_two, print_message, sum_list_of_numbers, sum_iterable_of_numbers, is_in, index_of_number

APP = Flask(__name__)

@APP.route('/multiply', methods=['GET'])
def multiply():
    incoming = request.get_json()
    return dumps(multiply_by_two(incoming['number']))

@APP.route('/print', methods=['GET'])
def message():
    incoming = request.get_json()
    return dumps(print_message(incoming['message']))

@APP.route('/sum/list', methods=['GET'])
def sum_list():
    incoming = request.get_json()
    return dumps(multiply_by_two(incoming['number']))

@APP.route('/sum/iterable', methods=['GET'])
def sum_iterable():
    incoming = request.get_json()
    return dumps(multiply_by_two(incoming['number']))

@APP.route('/is/in', methods=['GET'])
def isin():
    incoming = request.get_json()
    return dumps(is_in(incoming['needle'], incoming['haystack']))

@APP.route('/index', methods=['GET'])
def index():
    incoming = request.get_json()
    ret = index_of_number(incoming['item'], incoming['numbers'])
    return dumps(ret)

if __name__ == "__main__":
    APP.run(port=8000)
