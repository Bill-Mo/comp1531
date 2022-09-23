from flask import Flask, request
import json

app = Flask(__name__)

L = []
# Write your routes here
@app.route('/name/add', methods = ['POST'])
def add():
    global L
    n = request.args.get('name')
    if n is not None:
        L.append(n)
    return json.dumps({})
@app.route('/names', methods = ['GET'])
def names():
    return json.dumps(L)
@app.route('/name/remove', methods = ['DELETE'])
def remove():
    global L
    n = request.args.get('name')
    L.remove(n)
    return json.dumps({})
if __name__ == '__main__':
    app.run(port=0)
