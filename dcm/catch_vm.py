import os
import pymysql as mysql
import xml.etree.ElementTree as ET

db = mysql.connect(user='root',passwd='root',db='test',host='localhost')
db.autocommit(True)
cursor = db.cursor()

cursor.execute("select hostname from addvm_list")
results= cursor.fetchall()
for row in results:
    vmname = row[0]

tree = ET.parse('/var/kvm/%s.xml' %vmname)
root = tree.getroot()
global ins_uuid,ins_name,ip_addr,host_id,ram,vcpus,status
ins_uuid=root.find('uuid').text
ins_name=root.find('name').text
ram=root.find('memory').text
vcpus=root.find('vcpu').text
mac_addr=root.find('devices/interface/mac')
mac_addr=mac_addr.get('address')
searchip=os.popen('ip n |grep -i %s' %mac_addr).read()
ip_addr=searchip[0:searchip.rfind('dev',1)-1]
host_id=4
status=os.popen('virsh domstate %s' %ins_name).read()

sql="insert into instance_list(uuid,name,ip_addr,host_id,ram,vcpus,status) values('%s','%s','%s','%s','%s','%s','%s')"%(ins_uuid,ins_name,ip_addr,host_id,ram,vcpus,status)
cursor.execute(sql)
cleardata="TRUNCATE TABLE addvm_list"
cursor.execute(cleardata)
db.close()
print("VM data input")
#print ins_uuid,ins_name,ram,vcpus,ip_addr,host_id,status

#root.find('').text

#disk=root.find('devices/disk/source')
#disk=disk.get('file')

#host_id=os.popen('hostname').read()
#vm_id=os.popen('virsh domid %s' %ins_name).read()


#print ins_uuid,ins_name,ram,disk,vcpus,os_type,os_variant,network_bridge,ip_addr,host_id,status
#sql="INSERT INTO instance_list(ins_uuid,ins_name,ram,disk,vcpus) VALUES('%s','%s','%s','%s','%s')" %(ins_uuid,ins_name,ram,disk,vcpus)
