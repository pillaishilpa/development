import sys
import re
import random
print '-----welcome to cow and bull game-----------\n'
list1 = []
list2 = []
c=0
b=0
num = random.randint(1000,9999)
print num
number = str(num)
n=0
y=1
for ch in number:
	list1.append(ch)
while(y):
	if c == 0 and b == 0:
		print 'now you have %d cow and %d bull\n' %(c,b)
	else:
		print 'with your entered numer you have %d cows and %d bulls\n' %(c,b)
	n=+1
	print ' please enter a 4 digit number\n'
	a = input()
	num_in = str(a)
	for ch in num_in:
		list2.append(ch)
	c=0
	b=0
	for i in range(3):
		j=0
		for j in range(3):
			if list1[i]==list2[j]:
				if i==j:
					print '----------------incrementing cows--------------\n'
					c+=1
				else:
					print '-----------------incrementing bulls-------------\n'
					b+=1
			else:
					continue
	if num == a:
		print'---completed the game with %d attempt\n' %n
		break

