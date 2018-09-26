import sys
import os
import re
import os.path
import getpass



class Diagnostic_error (Exception):
     pass

class Invalide_file_formate(Exception):
     pass	 


def get_diagnostic_statement(file_name):  #takes the diagnostic word and generates "diagnostic dia_name on for session" statement
	file1 = open(file_name,"r")
	diag_file_map={}
	try:
		diagnostic_word_list = [word.strip() for word in open(file_name)]
		for i,j in enumerate(diagnostic_word_list,1):
		   diag_file_map[j]=i		
	except IOError as error:
	    print " \n File not found\n\t "+ str(error)
	#diagnostic_word_list=list(set(diagnostic_word_list))    
	test_diagnostic_words(diagnostic_word_list,diag_file_map)
	diagnostic_state_list=[]
	for word in diagnostic_word_list:
		word = "diagnostic "+word
		if word.lower() == "diagnostic random(50)":
			word = word+" for session;\n\n"
		else:
			word=word+" on for session;\n\n"
		diagnostic_state_list.append(word)
	file1.close()
	return diagnostic_state_list

def test_diagnostic_words(diagnostic_word_list,diag_file_map):   
	diag_file=[word.strip() for word in open("diagnostic_list.txt")]
	invalid_diagnostic=[]
	index=0;
	#print diagnostic_word_list
	if '' in diagnostic_word_list:
	   del diagnostic_word_list[diagnostic_word_list.index('')]
	try:
		while index < len(diagnostic_word_list):
			if (not diagnostic_word_list[index].lower() in diag_file) and (not diagnostic_word_list[index].upper() in diag_file):
			   if(not diagnostic_word_list[index] in diag_file):
			      invalid_diagnostic.append(diagnostic_word_list[index] + " in line " +str(diag_file_map.get(diagnostic_word_list[index])))
			      del(diagnostic_word_list[index])
			   else:
			      index=index+1
			else:
				index=index+1
		if  invalid_diagnostic: 
			
			raise Diagnostic_error("Invalid Diagnostic in list please verify diagnostic\n\n"+"\n".join(invalid_diagnostic)+" \n")
	except Diagnostic_error as error:
			print "\n********************************************************\n\n"
			print error;
			print "\n********************************************************\n\n"         

def validate_file(text_file,bteq_file):
	try:
		#print "\n",bteq_file
		
		if text_file.find(".txt")==-1 or (bteq_file.find(".bteq")==-1 and bteq_file.find(".sql")==-1):
				
				raise Invalide_file_formate("\n ***  Invalid File Input  ***")
	except Invalide_file_formate as error:
	        print error;sys.exit(0)
			
	
def Get_new_bteqFile_name(old_file_name):
	 new_file="new"+(old_file_name).split(".")[0] +"."+(old_file_name).split(".")[1]
	 return new_file
	 
	
def validate_file_cleanup(new_bteqFile,Bteq_file,index):
		while index < len(Bteq_file):
			if Bteq_file[index].lower().find("delete ")==0 or Bteq_file[index].lower().find("delete ") ==1:
				new_bteqFile.append(Bteq_file[index])
			elif Bteq_file[index].lower().find("del ")==0 or Bteq_file[index].lower().find("del ") ==1:	
				new_bteqFile.append(Bteq_file[index])
			elif Bteq_file[index].lower().find("drop ")==0 or Bteq_file[index].lower().find("drop ") ==1:
				new_bteqFile.append(Bteq_file[index])	
			elif Bteq_file[index].lower()=='\n':
				new_bteqFile.append(Bteq_file[index])
			else:
			   break
			index=index+1   
		if 	Bteq_file[index].lower().find(".logoff")!=-1 or Bteq_file[index].lower().find(".quit")!=-1 or \
		Bteq_file[index].lower().find(".logon ")!=-1 or Bteq_file[index+1].lower().find(".os ")==0:
			if Bteq_file[index].lower().find(".logon ")!=-1:
				return [index-1,-1]
			new_bteqFile+="\n"
			new_bteqFile.append(Bteq_file[index])
			return [index,-1]
		else:
			return [index,index]

			
def Export_file(new_bteqFile,Bteq_file,index,diagnostic_list):     
     while index < len(Bteq_file):
		if Bteq_file[index].upper().find(".SET DEFAULTS")>=0:
		  new_bteqFile.append(Bteq_file[index]) 
		  result=(validate_file_cleanup(new_bteqFile,Bteq_file,index+1))
		  if result[1] !=-1:
			 new_bteqFile+=(diagnostic_list)
			 new_bteqFile.append(Bteq_file[result[0]])
			 index=result[0]	
		  return result[0]
		new_bteqFile.append(Bteq_file[index]) 
		index+=1
		
def insert_repeat(new_bteqFile,index):
			
			new_bteqFile.insert(index,".repeat 50\n")
			return (0)
			

def validate_select(new_bteqFile):
	
	querry = []
	check_querry = 0
	check_export = -1
	check_querrybegan = 0
	ind = -1;
	list1 = ["select","sel"]
	list_not = ["create"]
	p = re.compile(".export",re.I)
	p1 = re.compile("select",re.I)
	p2 = re.compile("sel",re.I)
	flag_crt = 1
	i = -1
	length_bteq_file = len(new_bteqFile)
	#print length_bteq_file
	insert_flag = -1
	to_be_added_index= []
	new_bteq_File = []	
	for line in new_bteqFile:
		
		i = i+1
		if line.startswith('.'):
			if p.match(line): 
				if check_export == -1:
					check_export = 0
				elif check_export == 0:
					check_export = -1	
			continue		
		elif check_export == 0:			
			continue		
		elif (check_querrybegan == 0) and (re.match("^[a-zA-Z]+.*",line)):	
			
			querry.append(line)		
			check_querrybegan = 1
			ind = i
	
			if line.endswith(';\r\n') or line.endswith(';\n\n') or line.endswith(';\n'):	
				if p1.match(line) or p2.match(line):	
					if not(any(word in line for word in list_not)):	
						to_be_added_index.append(ind)
						insert_flag = 0		
				querry[:]=[]
				check_querrybegan = 0
				
				
		elif check_querrybegan == 1:
			querry.append(line);
			if line.endswith(';\n') or line.endswith(';\r\n') or line.endswith(';\n\n'):
				
				if p1.match(querry[0]) or p2.match(querry[0]):
					for querry_string in querry:
						if any(word in querry_string for word in list_not):
							flag_crt = 0;
							break;
					if flag_crt == 1:
						to_be_added_index.append(ind)
						insert_flag = 0
				querry[:]=[];	
				check_querrybegan = 0
				flag_crt = 1
	
	
	
	
	i = 0
	k = 0
	if len(to_be_added_index) == 0:
		return new_bteqFile
	val = to_be_added_index[len(to_be_added_index)-1]
	
	while i < len(new_bteqFile):
		if (to_be_added_index[k]) == i and k < (len(to_be_added_index)-1):
			k = k+1
			
			new_bteq_File.append(".repeat 50\n")
			
		if i == val:
			new_bteq_File.append(".repeat 50\n")
		new_bteq_File.append(new_bteqFile[i])
		i = i+1	
	return new_bteq_File
		
	
		
def Generate_new_bteqFile_content(Bteq_file,diagnostic_list):
		new_bteqFile=[]
		new_bteq_File = []
		index=0
		statement="diagnostic RANDOM(50) for session;\n\n"
		statement1="diagnostic random(50) for session;\n\n"
		#print "\n",User_list,"\n",Bteq_file,"\n",diagnostic_list
		print len(Bteq_file)
		while index < (len(Bteq_file)):		
			print index
			new_bteqFile.append(Bteq_file[index])
			if Bteq_file[index].upper().find(".EXPORT FILE")>=0:
				index=Export_file(new_bteqFile,Bteq_file,index+1,diagnostic_list)
			if Bteq_file[index].lower().find(".logon ")>=0 :
				if(Bteq_file[index].lower().find("/dbc")==-1 and \
   				Bteq_file[index].lower().find(",dbc")==-1) :
					if( Bteq_file[index+1].lower().find(".os ")==-1):#check for .os or any "." statements
					   result=(validate_file_cleanup(new_bteqFile,Bteq_file,index+1))
					#print result
					   if result[1] !=-1:
						 new_bteqFile+=(diagnostic_list)
						 new_bteqFile.append(Bteq_file[result[0]])
					   index=result[0]									
			index+=1
		if ((statement in diagnostic_list or statement1 in diagnostic_list)  and (statement in new_bteqFile or statement1 in new_bteqFile)):#check if random(50) in diagnostic list  
			new_bteqFile = validate_select(new_bteqFile)		
		return new_bteqFile    
def checkCreateFile(bteq_file):
	if(os.path.exists(os.path.abspath(bteq_file))):
		print "file found in current directory:"
	else:
		userName = raw_input("enter username:")
		pwd = getpass.getpass("Pasword:")
		
		
		
def main():
	try:
		checkCreateFile(sys.argv[2]);
		validate_file(str(sys.argv[1]),str(sys.argv[2]))
		diagnostic_list = get_diagnostic_statement(str(sys.argv[1]))
		file2 = open(str(sys.argv[2]),"r")
		Bteq_file=file2.readlines()
		new_file=Get_new_bteqFile_name(str(sys.argv[2]))
		result_bteqFile_content = Generate_new_bteqFile_content(Bteq_file,diagnostic_list)
		destination_file=open(new_file,"w")
		destination_file.writelines(result_bteqFile_content)
		destination_file.close()
	except IndexError as error:
		print "Format Error \n"
		print "\t format to be followed is \n"
		print "\t \t python <python file_name> <text file_name> <bteq file_name>"
	except IOError as error:
	    print " \n File not found\n\t "+ str(error)
	 
main()