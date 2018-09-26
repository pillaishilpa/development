import re
import os
import paramiko

try:
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect("10.25.33.61",username="root",password="Beagl342")
	print "connection established\n"
	stdin, stdout, stderr = ssh.exec_command("pcl -s pdestate -a")
	print(stdout.read())
	stdin, stdout, stderr =ssh.exec_command("rpcinfo -p ")
	print(stdout.read())
	ssh.exec_command("ctl")
	#stdin.write() can be used to provide the input to the command
	#for transferring file from local to remote or remote to local
except Exception as e:
	print str(e)+" error in ssh connection"