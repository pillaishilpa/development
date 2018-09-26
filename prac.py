import re
str1='shilpa'
str2='abcshhilpaaxyz'
flg=0
for ch in str1:
	if str2.count(ch)>=str1.count(ch):
		pass
	else:
		flg=1
		break
if flg==1:
	print 'not ok'
else:
	print 'ok'