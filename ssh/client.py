#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import MySQLdb

str=sys.argv[1].split('/')
vmip=str[0]
port=str[1]
keyname=str[2]
serverip=str[3]
serverkey=str[4]

cmd='python ssh12345_os.py %s/%s/%s'%(vmip,port,keyname)
cmd="sudo ssh root@%s -i %s %s"%(serverip,serverkey,cmd)
ddd = os.system(cmd)
print ddd
#print cmd

db = MySQLdb.connect("localhost","root","root","cloud" )

cursor = db.cursor()

sql = "INSERT INTO ssh_list(key_name,location,port ) \
       VALUES ('%s', '%s', '%s')" % \
       (keyname,vmip,port)

#print sql
try:
   cursor.execute(sql)
   db.commit()
   print 'insert success'
except:
   # Rollback in case there is any error
   print 'insert failed,rollbacked'
   db.rollback()

db.close()
