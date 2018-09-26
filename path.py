import os.path
import sys
import 	pxssh
obj = pxssh.pxssh()
server_name = raw_input('server_name:')
user_name = raw_input('user_name:')
passwd = getpass.getpass('password:')
obj.login(server_name,user_name,passwd)
obj.sendline('ls-l')
"""path = os.path.abspath(sys.argv[1])
if(os.path.exists(path)):
	print 'file exists\n'
else:
	print 'file not present\n' """
