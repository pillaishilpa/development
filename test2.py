from sys import argv
print "-----------------testing--------------"
script, filename = argv
print "inputs"
print "enter you name",
name = raw_input()
print " enter ur age",
age = int(raw_input())
print "enter ur salary",
sal = float(raw_input())
print " your name is %s\n your age is %d\n your sal is %f" % (name,age,sal)
fp = open(filename, 'r+')
print " displaying content of file %s\n" %filename
print fp.read()
print"trucating file %s" %filename
fp.truncate()
fp.close()
fp = open(filename ,'r+')
print"redind the file again\n"
print fp.read()
print"-------------\n"
print"writing new content in the file\n"
fp.write('learning python\n')
print" reading the file again\n"
print fp.read()
print"-----done-------\n"
fp.close()


