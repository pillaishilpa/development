import teradata
col = []

def connect_retrieve():
	
	user_name = raw_input("enter user name");
	udaExec = teradata.UdaExec (appConfigFile="PrintTableRows.ini")
	with udaExec.connect("${dataSourceName}") as session: 
		with session.cursor() as cursor:
			for row in cursor.execute(" SELECT trim(tablename) as tn FROM dbc.tables WHERE databasename ='"+user_name+"'"):
				col.append(row.tn)
	leng_r = len(col)
	print "\nNo. of tables:",leng_r,"\n"
	print "Tables List:"
	for i in col:
		print i
		print "sel * from",i
	fast_export_script(user_name);

def create_fastexportScript(data_infile,user_name):
	
	for j in range(len(col)):
		data_to_write = []
		for i in range(len(data_infile)):
			str_1 = data_infile[i]
			if ("&XXX" in str_1) & ("&XXXX" not in str_1):
				str_1 = str_1.replace("&XXX",user_name);
			elif "&XXXX" in str_1:
				str_1 = str_1.replace("&XXXX",user_name[:8]+"_"+col[j])
			elif "&TTT" in str_1:
				str_1 = str_1.replace("&TTT",col[j]);
			data_to_write.append(str_1);
		file_name = user_name[:8]+"_"+col[j]+".fe";
		fast_export_file = open(file_name,'w');
		fast_export_file.writelines(data_to_write);
		
def fast_export_script(user_name):
	data_infile = [];
	template_file = open('fastexport_template.fe','r');
	data_infile= template_file.readlines();
	create_fastexportScript(data_infile,user_name)
	

connect_retrieve();
	
	

       
     



