#! /usr/bin/python
import libvirt
import sys, os

def domainStateToString(state):
    sts = ('no state', 'running', 'blocked', 'suspended', 'shutting down', 'shut off', 'crushed')
    return sts[state]


def getInfo():
    if len(sys.argv) < 2:
      uri = 'qemu:///system'
    else:
      uri = sys.argv[1]

    conn = libvirt.open(uri)

    if conn is None:
      print >> sys.stderr, "Could not connect to VMM: %s" % uri
      sys.exit(1)

    try:
      vms = [(i, conn.lookupByID(i)) for i in conn.listDomainsID()]
      res = [(i, vm.name(), domainStateToString(vm.info()[0])) for (i,vm) in vms]
      print "%3s %-20s %s" % ('Id', 'Name', 'State')
      print "----------------------------------"
      for r in res:
        print "%3s %-20s %s" % r

      for name in conn.listDefinedDomains():
        dom = conn.lookupByName(name)
        print "%3s %-20s %s" % ("-", dom.name(),"down")

    except:
        print >> sys.stderr, "Could not get the list"