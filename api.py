#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps

from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'hello:)'

@app.route('/api/<instance_id>', methods=['POST'])
def startup(instance_id):
    return 'hello:)' % instance_id

@app.route('/api/instances/<instance_id>', methods=['GET'])
def status():
    return 'hello:)'

@app.route('/api/instances/<instance_id>', methods=['GET'])
def delete(instance_id):
    return 'hello:)' % instance_id

if __name__ == '__main__':
    app.run()
