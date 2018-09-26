import re
import os
import paramiko
import time
start_time=time.time()
try:
  ssh=paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect("10.25.33.61",username="root",password="Beagl342")
  print "connection established\n"
  stdin,stdout,stderr=ssh.exec_command("pdestate -a")
  print(stdout.read())
  #stdin,stdout,stderr=ssh.exec_command("cd {};pwd".format("/opt/td"))
  stdin,stdout,stderr=ssh.exec_command("cd /opt/td;pwd;")
  print (stdout.read())
except Exception as e:
  print str(e) + "error in connection"
print "exwecution time is",time.time()-start_time