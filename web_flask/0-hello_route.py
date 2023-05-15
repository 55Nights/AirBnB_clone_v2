#!/usr/bin/python3
""" Contains a minimam flask Application"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """Returns A string hello world"""
    return 'Hello, World!'