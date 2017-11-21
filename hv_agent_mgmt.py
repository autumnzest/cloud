#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys, libvirt
import hv_agent_getinfo

conn = libvirt.open('qemu:///system')
if conn is None:
    print 'Failed to open connection to qemu:///system'
    exit(1)

def proc(name, num):
    vm = conn.lookupByName( name )
    st = int(num)

    if st == 1:
       vm.create()
       print "Starting " + vm.name()
    elif st == 2:
       vm.suspend()
       print "Suspending " + vm.name()
    elif st == 3:
       vm.resume()
       print "Resuming " + vm.name()
    elif st == 4:
       vm.destroy()
       print "Stopping " + vm.name()
    else:
       exit(1)

if __name__ == '__main__':
    hv_agent_getinfo.getInfo()

    try:
        input1 = raw_input('Please input the name of vm: ')
        x = str(input1)
        input2 = raw_input('Please select -> start=1, suspend=2, resume=3, destroy=4: ')
        y = int(input2)
    except ValueError:
        print('Please input the correct information')
    proc(x, y)