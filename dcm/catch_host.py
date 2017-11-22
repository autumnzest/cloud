from datetime import datetime
import os
import platform
import psutil
import pymysql as mysql

db = mysql.connect(user='root',passwd='Root%123',db='cloud',host='kvmhost01')
db.autocommit(True)
cur = db.cursor()
###catch###
hostname=platform.node()

disk=os.statvfs("/home")
hd = round(disk.f_bsize * disk.f_bavail/1024/1024/1024)
hdc = round(disk.f_bsize * disk.f_blocks/1024/1024/1024)
hdu = round(disk.f_bsize * disk.f_bfree/1024/1024/1024)
'''
                global memory
                memory=round(psutil.virtual_memory()[0]/1024/1024)
                return memory

#host_id=os.popen('hostid').read()
#ccheck="SELECT hostname FROM dcm WHERE hostname='%s'"%hostname
#a=pandas.read_sql(check,db)
#print (a)
'''

#sql="insert into host_list(host_name,available,total,used) values('%s',%s,%s,%s)"%(hostname,hd,hdc,hdu)
sql="update host_list set available='%s',used='%s',updated_at=NOW() where host_name='%s'"%(hd,hdu,hostname)
cur.execute(sql)
#print ('S4 data input')
print ('Updata S4 ok')
