tbl=['']*10
def hash_fun(val):
	return val%len(tbl)

def insert(val,data):
	key=hash_fun(val)
	if tbl[key]=='':
		tbl[key]=(val,data)
	elif type(tbl[key])==tuple:
		prv_val=tbl[key]
		tbl[key]=[]
		tbl[key].append(prv_val)
		tbl[key].append((val,data))
		tbl[key].sort(key= lambda val:val[0])
	else:
		tbl[key].append((val,data))
		tbl[key].sort
		
def search(val,data):
	i=0
	key=hash_fun(val)
	if type(tbl[key])==list:
		for value in tbl[key]:
			if data and val in value:
				return key,i
				break
			i+=1
		return -1,0
	elif data in tbl[key]:
		return -2,key
	else:
		return -1,0

def del_elm(val,data):
	index=search(val,data)
	if index[0]==-1:
		print "Element not found"
	elif index[0]==-2:
		tbl[index[1]]=""
	else:
		tbl[index[0]][index[1]]=""

