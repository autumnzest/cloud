import os
import sys
import pymysql as mysql
import time
###catch addvm data#
add_name=input("Input the name of VM:")
add_memory=input("Input the size of memory:")
add_disk=input("Input the size of disk:")
add_ip=input("Input the hope of IP Address(Emtry is ok):")
add_admin=input("Input the admin of VM:")


###updata the free disk###
#os.system("ssh root@192.168.1.3 -i ~/.ssh/key2 'python catch_host.py' ")
#time.sleep(2)
os.system("ssh root@192.168.1.4 -i ~/.ssh/key3 'python ~/cloud/dcm/catch_host.py' ")
#time.sleep(2)
#os.system("ssh root@192.168.1.5 -i ~/.ssh/key4 'python catch_host.py' ")
###updata vmname###

###check vmname###
db = mysql.connect(user='root',passwd='root',db='test',host='localhost')
db.autocommit(True)
cursor = db.cursor()
checkname="SELECT * FROM instance_list WHERE name='%s'" %add_name
cursor.execute(checkname)
check = cursor.fetchall()
'''
if check:
    print "Error: An VM of the same name already exists."
else:
    print "hostname:'%s' is ok!" %add_name
'''
###manager###

checkdisk = "SELECT host_name,total FROM host_list WHERE total >'%s' ORDER BY RAND() LIMIT 1" %add_disk
cursor.execute(checkdisk)
results = cursor.fetchall()
for row in results:
    server_name = row[0]
    free_disk = row[1]
db.close()
###write data to cloud.addvm##
db = mysql.connect(user='root',passwd='root',db='test',host='localhost')
db.autocommit(True)
cursor = db.cursor()
writeadd="INSERT INTO addvm_list(hostname,memory,disk,network,admin) VALUES('%s',%s,%s,'%s','%s')" %(add_name,add_memory,add_disk,add_ip,add_admin)
cursor.execute(writeadd)

###ADD VM###
print('The new VM in %s' %(server_name))
time.sleep(2)
keynumber=int(server_name[-1])
addcmd="ssh root@%s -i key%s 'python cloud/dcm/createvm_xml.py'" %(server_name,keynumber)
os.system(addcmd)
new_disk=int(float(free_disk)-float(add_disk))
updatedisk="UPDATE host_list SET total='%s' WHERE host_name='%s' " %(new_disk,server_name)
try:
        cursor.execute(updatedisk)
except:
        print("Error: unable to fecth data")
db.close()
print('The disk of %s updated.' %server_name)
