print '------testing------\n'
import sys
import re
file1 = sys.argv[1]
print file1
file2 = sys.argv[2]
fa = open(file1,'r+')
fb = open(file2,'w+')
for line in fa.readlines():
	print line
fa.cloe()
fb.close()