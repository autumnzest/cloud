#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import database
#import accesslibrary
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, url_for, abort, Response, render_template

app = Flask(__name__)
#TODO:testをcloudに
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

instance_list_class = database.instance_list

@app.route('/cloud', methods=['GET'])
def home():
    instance_list = instance_list_class.query.all()
    return render_template('index.html', list=instance_list)

#新規インスタンス起動
@app.route('/api/instances/', methods=['POST'])
def startup(instance_id):
    return 'instance{}'.format(instance_id)

#インスタンスの状態をチェック
@app.route('/api/instances/<string:instance_id>', methods=['GET'])
def status(instance_id):
    status = instance_list_class.query.filter_by(id=instance_id).one()
    return format(status.status)

#インスタンスの終了
@app.route('/api/instances/<string:instance_id>', methods=['DELETE'])
def delete(instance_id):
    return 'instance{}'.format(instance_id)

#@app.route('/api/pubkey', methods=['GET'])
#def get_pubkey():
#    return ''

#@app.route('/api/pubkey/<string:pubkey_id>', methods=['GET'])
#def get_pubkey():
#    return ''

#@app.route('/api/pubkey/<string:pubkey_id>', methods=['GET'])
#def get_pubkey_id():
#    return ''


if __name__ == '__main__':
    app.run()
