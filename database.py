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
    ip_addr = db.Column(db.String(20))
    host_id = db.Column(db.Integer)
    autostart = db.Column(db.String(5))
    ssh_id = db.Column(db.Integer)
    ram    = db.Column(db.Integer)
    vcpus   = db.Column(db.String(10))
    status   = db.Column(db.DATETIME)
    created_at  = db.Column(db.DATETIME)
    updated_at  = db.Column(db.DATETIME)

    def __init__(self, id, uuid, name, ip_addr, host_id, autostart, ssh_id, ram, vcpus, status, created_at, updated_at):
        self.id     = id
        self.uuid   = uuid
        self.name   = name
        self.ip_addr= ip_addr
        self.host_id= host_id
        self.autostart=autostart
        self.ssh_id = ssh_id
        self.ram = ram
        self.vcpus = vcpus
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at


