import re
import inspect
from collections import Counter
#src = inspect.getsource(re)
#print src
"""def minion_game(s):
	s=s.upper()
	kevin=[];stuart=[];
	vovel=['A','E','I','O','U']
	i=0
	while(i<len(s)):
		j=i+1;k=1
		if s[i] in vovel:
			kevin.append(s[i])
			while(j<len(s)):
				kevin.append(kevin[k-1]+s[j])
				j+=1
				k+=1
		else:
			stuart.append(s[i])
			while(j<len(s)):
				stuart.append(stuart[k-1]+s[j])
				j+=1
				k+=1
		i+=1
	kevin_counter=Counter(kevin)
	kevin_count=sum(kevin_counter.values())
	stuart_counter=Counter(stuart)
	stuart_count=sum(stuart_counter.values())
	print kevin_count,stuart_count
	if kevin_count>stuart_count:
		print 'Kevin  ',kevin_count
	else :
		print 'stuart  ',stuart_count
"""
def minion_game(string):
    # your code goes here
    s=string.upper()
    kevin=[];stuart=[];
    vovel=['A','E','I','O','U']
    i=0
    while(i<len(s)):
        j=i+1;k=1
        if s[i] in vovel:
            kevin.append(s[i])
            while(j<len(s)):
                kevin.append(kevin[k-1]+s[j])
                j+=1
                k+=1
        else:
            stuart.append(s[i])
            while(j<len(s)):
                stuart.append(stuart[k-1]+s[j])
                j+=1
                k+=1
        i+=1
    kevin_counter=Counter(kevin)
    kevin_count=sum(kevin_counter.values())
    stuart_counter=Counter(stuart)
    stuart_count=sum(stuart_counter.values())
    if kevin_count==stuart_count:
        print 'Draw'
    elif kevin_count>=stuart_count:
        print 'Kevin',kevin_count
    else:
        print 'Stuart',stuart_count
		
def main():
	s=raw_input('enter a string:')
	s=s.upper()
	minion_game(s)

if __name__=='__main__':
	main()
