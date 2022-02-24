import imp
from urllib import request
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json})
    else:
        return jsonify ({"about": "Hello World!!!"}) 

@app.route('/<string:marke>/<string:model>/<string:jahr>', methods=['GET'])
def data(marke, model, jahr):
        return jsonify({'brand': marke, 'model': model, 'year': jahr})


@app.route("/cars")
def cars():
    return jsonify({"brand": "Nissan", "model": "Skyline R34", "year": 2004})