
def chk_pal(l):
	i=0;j=len(l)-1
	while(i<=j):
		if(l[i]!=l[j]):
			break
		i+=1;j-=1
	if (i>j):
		return 1
		
def main():
	sum=0
	for num in range(1000000):
		l=[int(x) for x in str(num)]
		if(chk_pal(l)):
			bin='{0:b}'.format(num)
			if(chk_pal(bin)):
				print num , "      ",bin
				sum+=num
	print "the total sum of pallindrome numbers is",sum
if __name__=="__main__":
	main()
