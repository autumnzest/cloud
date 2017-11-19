#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess
import libvirt
import random
import string

def shutdown(params):

    server_name = 'root@192.168.1.3:52051/system?keyfile=~/.ssh/key2'
    c = libvirt.open('qemu+ssh://' + server_name)

    name = params['name']

    vm = c.lookupByName(name)

    vm.shutdown()


def destroy(params):

    server_name = 'root@192.168.1.3:52051/system?keyfile=~/.ssh/key2'
    c = libvirt.open('qemu+ssh://' + server_name)

    name = params['name']

    vm = c.lookupByName(name)

    vm.destroy()


if __name__ == '__main__':
    ##for debug
    cmd = {"name":"hoge"}
    install(cmd)
