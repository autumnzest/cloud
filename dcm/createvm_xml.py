import os
import sys
import pymysql as mysql
import xml.etree.ElementTree as ET
import random
import time

###catch add data###
db=mysql.connect(user='root',passwd='Root%123',db='cloud',host='kvmhost01')
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
os.system('cp /var/kvm/images/basevm.img /var/kvm/images/%s.img' %(addvm_hostname))

newmac = [ 0x00, 0x16, 0x3e,
           random.randint(0x00, 0x7f),
           random.randint(0x00, 0xff),
           random.randint(0x00, 0xff) ]
addmac=(':'.join(map(lambda x: "%02x" % x, newmac)))

tree = ET.parse('/var/kvm/basevm.xml')
root = tree.getroot()
vmname = root.find('name')
vmname.text="%s" %addvm_hostname

newuuid=os.popen('uuidgen - UUID').read()
vmuuid = root.find('uuid')
vmuuid.text="%s" %newuuid

a=int(addvm_memory)
addmemory=a*1024
vmmemory = root.find('memory')
vmmemory.text="%s" %addmemory
print(vmmemory.text)

newsource="/var/kvm/images/%s.img" %addvm_hostname
vmsource = root.find('devices/disk/source')
vmsource.set('file','%s' %(newsource))

vmmac = root.find('devices/interface/mac')
vmmac.set('address','%s' %(addmac))

tree.write("/var/kvm/%s.xml" %(addvm_hostname))


###run###
define="virsh define /var/kvm/%s.xml" %(addvm_hostname)
os.system(define)
start="vish start %s"%(addvm_hostname)
os.system(start)
time.sleep(10)
print("Installed in server4")
os.system('python catch_vm.py')