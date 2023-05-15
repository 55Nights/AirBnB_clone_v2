#!/usr/bin/python3
""" Contains a minimam flask Application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns A string hello world"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return "“HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
