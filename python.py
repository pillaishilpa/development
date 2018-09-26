print '--------testing-----\n'
import sys
import re
file1 = sys.argv[1]
file2 = sys.argv[2]
fa = open(file1,'r+')
fb = open(file2,'w+')
for line in fa:
	print 'reading file content-----\n'
	print line
fa.close()
