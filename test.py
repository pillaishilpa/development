import re
import pdb
"""str1=raw_input('enter a string:')
nw_str=[]
i=1
cnt=1
while(i<len(str1)):
	if str1[i]==str1[i-1]:
		cnt+=1
	else:
		nw_str.append(str1[i-1])
		nw_str.append(str(cnt))
	i=i+1
print nw_str"""
#decorators
"""def parent(msg):
	print 'inside parent fun\n'
	def child1():
		print 'imside child2\n'
	def child2():
		print 'inside child2\n'
@parent
def dec(msg):
	return msg
print dec("HEllo")"""
# to print the top 10 most frequesnt words used in the file
"""count={}
lst=[]
with open("input.txt") as fo:
	for line in fo:
		lst=line.split()
		for word in lst:
			if word in count:
				count[word]+=1
			else:
				count[word]=1
for key,val in count.items():
	lst.append((val,key))
lst.sort(reverse=True)
print lst[:10]"""
# pdb testing
"""
import pdb
l=[]
for i in range(10):
	l.append(i)
	pdb.set_trace()
print i"""
d={}
count=0
with open("input.txt") as fo:
	for line in fo:
		l=line.split()
		for val in l:
			if val in d:
				d[val]=d[val]+1
			else:
				d[val]=1
	pdb.set_trace()
	
		