#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, url_for, abort, Response, render_template

app = Flask(__name__)
#TODO:testをcloudに
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class instance_list(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(80))
    name = db.Column(db.String(200))
    status   = db.Column(db.String(10))

    def __init__(self, uuid, name, status):
        self.uuid   = uuid
        self.name   = name
        self.status = status


