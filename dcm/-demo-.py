from __future__ import print_function
import sys
import libvirt
class switch(object):
	"""docstring for switch"""
	def __init__(item,hostname):
		item=0;
		hostname=0;
def __int__(self):
	self.conn()

def conn():
  	conn = libvirt.open('qemu:///system')
  	if conn == None:
    	 print('Failed to open connection to qemu:///system')
         exit(1)

	domainName = 'kvm_centos7'
	dom = conn.lookupByName(domainName)


def select():
	print( '''
        ----------------------------
                1 Add
                2 Start
                3 Shutdown
                4 Del
                5 Exit
        ----------------------------
                ''')
	while True:
		item=input('Number:')
		if not item:break
		if item==1:
			create()
		if item==2:
			start()
		if item==3:
			shutdown()
		if item==4:
			delete()
		if item==5:
			print ('See you!')
			exit(1)
		break
######create#########
def create(): 
	
os.system("virt-install --name vm2 --ram 4096 --disk path=/var/kvm/images/vm2.img,size=30 --vcpus 2 --os-type linux --os-variant rhel7 --network bridge=virbr0 --graphics none --console pty,target_type=serial --location 'http://ftp.iij.ad.jp/pub/linux/centos/7/os/x86_64/' --extra-args 'console=ttyS0,115200n8 serial' --check all=off")
	#hostname=input('Hostname:')
	#memory=input('Memory:')
	#disk=input('Disk:')
	#cmd="sudo virt-install --name %s --ram %s --disk path=/vm/%s.img,size=%s"%(hostname,memory,hostname,disk)
	#os.system("sudo virt-install --name cen7 --ram 1024 --disk path=/vm/centos7.img,size=8 --vcpus 2 --os-type linux --os-variant rhel7 --network bridge=virbr0 --graphics none --console pty,target_type=serial --location 'http://ftp.iij.ad.jp/pub/linux/centos/7/os/x86_64/' --extra-args 'console=ttyS0,115200n8 serial' --check all=off")
	
	#xmldesc='''   '''
	#conn.defineXML(xmldesc)
	#dom=conn.createLinux(xmldesc,0)
	#print ("Domain:id %d running %s")% (dom.ID(),dom.OSType())

######handle######

####start####os.system("virch start $domainName")
def start():
	#hostname=input('Hostname:')
	hostname='vm1'
	domain=host.lookupByName(hostname)
	ret = domain.create()
    if ret == 0:
        return True
    return False

####shutdown####
def shutdown():
	hostname='vm1'
	#hostname=input('Hostname:')
	print(os.system('virsh shutdown %s')%hostname)
  	'''dom = _get_dom(hostname)  
    return dom.shutdown() == 0  '''

####del####
def delete():
	hostname=input('Hostname:')
	dom = _get_dom(hostname)  
    return dom.delete() == 0
####reboot####



if __name__=='__main__':
        select()






'''

import paramiko

def ssh2(ip,username,passwd,key,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,key,timeout=5)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print stdout.read()
        print '%stOKn'%(ip)
        ssh.close()
    except :
        print '%stErrorn'%(ip)
ssh2("192.168.1.3","root","root","key2","df")
ssh2("192.168.1.4","root","root","key3","df")
ssh2("192.168.1.5","root","root","key4","df")

