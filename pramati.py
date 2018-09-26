import re
import py_compile
py_compile.compile('pramati.py')
def abc(a,b=1):    #this is an error as  non-default argument follows default argument
	return a+b
def main():
	res=abc(8,9)
	print res

	class A:
		a=1
		def fun1(self):
			self.a=2
	obj=A()
	print obj.a
	obj.fun1()
	print obj.a

if __name__=="__main__":
	main()


	