import sys
def egy_frc(num,denum):	
	if (denum%num):
		temp= (denum/num)+1;
		sys.stdout.write( "1/%d +" %(temp))
		temp_nu=(temp*num - denum);
		temp_deno= denum*temp;
		egy_frc(temp_nu,temp_deno);
	else:
		temp=denum/num
		print ( "1/%d" %(temp))
def main():
	try:
		num=int(raw_input('enter the numerator value: '))
		denum=int(raw_input('enter the denominator value: '))
		if num<=0 or denum<=0 or num>denum:
			print 'invalid entry please enter a value greater than 0 with  denominator greater than numerator\n'
			return
		egy_frc(num,denum)
	except Exception as e:
		print "please enter an integer value greater than ZERO"
	
if __name__=="__main__":
	main()
	