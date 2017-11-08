#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps

from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hello:)'

@app.route('/api/<string:instance_id>', methods=['POST'])
def startup(instance_id):
    return 'instance{}'.format(instance_id)

@app.route('/api/instances/<string:instance_id>', methods=['GET'])
def status(instance_id):
    return 'instance{}'.format(instance_id)

@app.route('/api/instances/<string:instance_id>', methods=['DELETE'])
def delete(instance_id):
    return 'instance{}'.format(instance_id)

if __name__ == '__main__':
    app.run()
