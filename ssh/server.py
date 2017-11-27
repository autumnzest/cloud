#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
str=sys.argv[1].split('/')
vmip=str[0]
port=str[1]
keyname = str[2]

cmd='ssh -C -f -N -g -L %s:%s:22 root@%s'%(port, vmip, vmip)
cmd2='ssh -C -f -N -g -R %s:localhost:%s zhang@192.168.1.2 -p 52051 -i id_rsa'%(port,port)
cmd3='firewall-cmd --zone=public --add-port=%s/tcp'%port
cmd4='ssh-keygen -t rsa -N cloud -f ~/.ssh/%s'%keyname
#cmd5='scp -i ~/.ssh/id_rsa ~/.ssh/authorized_keys root@%s:.ssh/authorized_keys'%vmip
cmd5='cat ~/.ssh/%s.pub | ssh -i ~/.ssh/id_rsa root@%s "cat - >> ~/.ssh/authorized_keys"'%(keyname,vmip)
cmd6='scp -i id_rsa -P 52051 ~/.ssh/%s zhang@192.168.1.2:%s'%(keyname,keyname)


try:
#       rel1 = os.system(cmd)
#       rel2= os.system(cmd2)
        rel1 = os.popen(cmd)
        rel2= os.popen(cmd2)
        rel3= os.system(cmd3)
        rel4= os.system(cmd4)
        rel5= os.system(cmd5)
        rel6= os.system(cmd6)

except Exception,e:
        pass
print rel1
print rel2
print rel3
print rel4
print rel5
print rel6
#os._exit()
#print cmd
#print cmd2
#print cmd3
#print cmd4
#print cmd5
#print cmd6
