print '-----------------testing--------------\n'
import sys
import re
file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
file_name3 = sys.argv[3]
fp = open(file_name1,'r+')
fn = open(file_name2,'w+')
fo = open(file_name3,'w+')
list1 = []
list2 = []
# print fp.read()
for line in fp.readlines():
		list1.append(line)	
i = 0
j =0
k =0
flag=1
for line in list1 :
		del list2[:]
		i=k
		#print list1[0].split()[0]
		match1 = re.search(';$' , line)
		match3 = re.search(r'Failure',list1[k])
		if match1 and (re.search('.*',list1[k]) or (list1[k].split()[0]).isalpha()):
			j+=1
			match2 = re.search(r'Failure',list1[k+1])
			if match2:
				fn.write(line)
			else :
				fo.write(line)
		#elif list1[k].split()[0]=='select' or list1[k].split()[0]=='sel':
		elif match3:
			pass
		else:
			print line
			while(flag):
				print list1[i]
				match = re.search(';$',list1[i])
				list2.append(list1[i])
				if match:
					pass
				else:
					i+=1
				if match:
					flag=0
			match2 = re.search(r'Failure',list1[i+1])
			if match2:
					for ch in list2:
						fn.write(ch)
			else:
					for ch in list2:
						fo.write(ch)	
			k=i
		k+=1
		
		
fp.close()
#fn.close()