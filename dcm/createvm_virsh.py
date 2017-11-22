import os
import sys
import pymysql as mysql
import xml.etree.ElementTree as ET
import random
import time

###catch add data###
db=mysql.connect(user='root',passwd='root',db='test',host='localhost')
cursor = db.cursor()
sql = "SELECT * FROM addvm_list"

try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
       addvm_hostname = row[0]
       addvm_memory = row[1]
       addvm_disk = row[2]
       addvm_network = row[3]
       addvm_admin= row[4]
except:
   print "Error: unable to fecth data"

db.close()
###updata xml ###



###run###
install="virt-install --name '%s' --ram '%s' --disk path=/var/kvm/images/'%s'.img,size='%s' --vcpus 2 --os-type linux --os-variant rhel7 --network bridge=virbr0 --graphics none --console pty,target_type=serial --location 'http://ftp.iij.ad.jp/pub/linux/centos/7/os/x86_64/' --extra-args 'console=ttyS0,115200n8 serial' --check all=off" %(addvm_hostname,addvm_memory,addvm_hostname,addvm_disk)
os.system(install)

time.sleep(10)
print("Installed in server4")
os.system('virsh dumpxml %s > %s.xml'%addvm_hostname)
os.system('python catch_vm.py')
