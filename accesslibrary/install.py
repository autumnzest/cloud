#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import subprocess
import libvirt
import random
import string

def install(params):

    server_name = 'root@192.168.1.3:52051/system?keyfile=~/.ssh/key2'
    c = libvirt.open('qemu+ssh://' + server_name)

    name = params['name'] if 'name' in params.keys() else random_string(5)
    vcpu = params['vcpu'] if 'vcpu' in params.keys() else 1
    ram = params['ram'] if 'ram' in params.keys() else 1024

    domain_ids = c.listDomainsID()

    for id in domain_ids:
        vm = c.lookupByID(id)
        if name == vm.name():
            return

    cmd = 'virt-install --name={0} --vcpus={1} --ram={2} \
--location=http://mirror.centos.org/centos/7/os/x86_64/ \
--disk path=/var/kvm/disk/{0}.qcow2,format=qcow2,size=8 \
--network bridge=virbr0 \
--arch=x86_64 \
--os-type=linux \
--os-variant=rhel7 \
--connect=qemu+ssh://{3} \
--nographics -v -x "console=ttyS0"'.format(name, vcpu, ram, server_name)

    ## for debug
    print(cmd) 
    #subprocess.call(cmd,shell=True)

    return 1

def random_string(length, seq='0123456789abcdefghijklmnopqrstuvwxyz'):
    sr = random.SystemRandom()
    return ''.join([sr.choice(seq) for i in range(length)])


if __name__ == '__main__':
    cmd = {"name":"hoge"}
    install(cmd)
