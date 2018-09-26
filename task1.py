import hash
def main():
	hash.insert(10,'shilpa')
	hash.insert(25,'rajin')
	hash.insert(20,'rupesh')
	hash.insert(15,'sudha')
	hash.insert(35,'unni')
	hash.insert(35,25)
	hash.insert(63,'mohan')
	hash.insert(88,'paru')
	hash.insert(44,'kuttu')
	index=hash.search(63,'mohan')
	if index[0]==-1:
		print "record searched not found"
	else:
		print 'record found'
	index=hash.search(99,'xyz')
	if index[0]==-1:
		print "record searched not found"
	else:
		print 'record found'
	hash.del_elm(35,'unni')
	hash.del_elm(97,'deepti')
	hash.insert(100,'monu')
	hash.insert(653,'rupesh')
	print hash.tbl
if __name__ == "__main__":
	main()