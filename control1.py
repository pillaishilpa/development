print '-------------------testing-------------\n'
import sys
import re
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
fo = open(file1,'r+')
fa = open(file2,'w+')
fb = open(file3,'w+')
#-------------
i=0
for line in fo:
	print 'line inside for loop is---',line
	i+=1
	print i
	try:
		match = re.search(';$',line)
		if match and(re.search('.*',line) or line.split()[0].isalpha()):
			print 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\n'
			pos = fo.tell()
			next_line = fo.next()
			fo.seek(pos)
			print 'next_line is ----',next_line
			print line
			#print fo.tell()
			match = re.search(r'Failure',next_line)
			if match:
				print 'next_line is ----',next_line
				print 'failure-----',line
				fa.write(line)
			else:
				fb.write(line)
		elif re.search(r'Failure',line):
			continue
		else:
			str = ''.join(line)
	except StopIteration:
		break
#except StopIteration:
		