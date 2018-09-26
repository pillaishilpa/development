print '----testing----\n'
import sys
import re
file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]
fo = open(file1,'r+')
fa = open(file2,'w+')
fb = open(file3,'w+')
list1 =[]
list2=[]
i = 0
flg = 1
for line in fo:
	print line
	# list1.append(line)
"""nt len(list1)
for line in list1:
	match = re.search(';$',line)
	if match and (list1[i].split()[0]).isalpha():
		if (i+1<len(list1)):
			match = re.search(r'Failure',list1[i+1])
		if match:
			fa.write(line)
		else:
			fb.write(line)
	elif (list1[i].split()[0]=='select' or list1[i].split()[0]=='sel'):
		k=i
		while(flg):
			match = re.search(';$',list1[i])
			if match:
				list2.append(list1[k])
				flg = 0
			else:
				list2.append(list1[k])
				k+=1
		if(k+1<len(list1)):
			i=k+1
		match = re.search(r'Failure',list1[i+1])
		if match:
			for ch in list2:
				fa.write(ch)
		else:
			for ch in list2:
				fb.write(ch)
	i+=1 """