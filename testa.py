print '--------testing-----\n'
import sys
import re
file1 = sys.argv[2]
file2 = sys.argv[3]
fa = open(file1,'r+')
fb = open(file2,'w+')
for line in fa:
	print line
fa.close()
fb.close()


