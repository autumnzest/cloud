#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import database
import accesslibrary
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


######API群######

#新規インスタンス起動
@app.route('/api/instances/', methods=['POST'])
def startup():
    name = request.form['name']
    vcpu = request.form['vcpu']
    ram = request.form['ram']

    ins = instance_list_class(name=name, vcpus=vcpu,ram=ram, status="starting")
    db.session.add(ins)
    db.session.commit()
    db.session.close()

    params = {"name":"name", "vcpu":"vcpu", "ram":"ram"}

    res = accesslibrary.install.install(params)

    instance_data = instance_list_class.query.filter(name==name).first()
    instance_data.status = "initializing"

    current_db_sessions = db.session.object_session(instance_data)
    current_db_sessions.add(instance_data)
    current_db_sessions.commit()
    current_db_sessions.close()

    return 'instance{}'.format(name)

#インスタンスの状態をチェック
@app.route('/api/instances/<string:instance_id>', methods=['GET'])
def status(instance_id):
    status = instance_list_class.query.filter_by(id=instance_id).one()
    return format(status.status)

#インスタンスの終了
@app.route('/api/instances/<string:instance_id>', methods=['DELETE'])
def delete(instance_id):
    return 'instance{}'.format(instance_id)


if __name__ == '__main__':
    app.run()
