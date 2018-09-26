import sys
def main():
	try:
		num=int(raw_input('enter the numerator value: '))
		denum=int(raw_input('enter the denominator value: '))
		if num==0 or denum==0 or num>denum:
			print 'invalid entry please enter a value greater than 0 with numerator greator than denominator\n'
			return
		temp=2
		final=num*1.0/denum
		print final
		sum=0
		while(1):
			sum+=1.0/temp
			if(sum == final):
				sys.stdout.write("1/%d" %(temp))
				return
			if(sum > final):
				sum-=1.0/temp
			else:
				sys.stdout.write("1/%d +" %(temp))
			temp+=1
	except Exception as e:
		print "please enter an integer value greater than ZERO"
	
main()