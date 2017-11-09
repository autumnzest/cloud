#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)
#TODO:testをcloudに
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

#TODO:test_dataをinstance_listに
class test_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instance_name= db.Column(db.String(80), unique=True)

    def __init__(self, instance_name):
        self.instance_name = instance_name

@app.route('/cloud', methods=['GET'])
def home():
    instance_list = test_data.query.all()
    return 'hello:)'

@app.route('/api/instances/<string:instance_id>', methods=['POST'])
def startup(instance_id):
    return 'instance{}'.format(instance_id)

@app.route('/api/instances/<string:instance_id>', methods=['GET'])
def status(instance_id):
    return 'instance{}'.format(instance_id)

@app.route('/api/instances/<string:instance_id>', methods=['DELETE'])
def delete(instance_id):
    return 'instance{}'.format(instance_id)

@app.route('/api/pubkey', methods=['GET'])
def get_pubkey():
    return ''

@app.route('/api/pubkey/<string:pubkey_id>', methods=['GET'])
def get_pubkey():
    return ''

@app.route('/api/pubkey/<string:pubkey_id>', methods=['GET'])
def get_pubkey_id():
    return ''


if __name__ == '__main__':
    app.run()
