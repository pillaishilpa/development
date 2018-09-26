import re
import os
import paramiko
try:
  ssh=paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect("153.64.30.80",username="root",password="Beagl342")
  print "connection established\n"
  stdin,stdout,stderr=ssh.exec_command("pdestate -a" and "pdepath -i")
  print(stdout.read())
  stdin,stdout,stderr=ssh.exec_command("cd /opt/td" and "upgrade_efix_revised")
  print(stdout.read())
except Exception as e:
  print str(e) + "error in connection"