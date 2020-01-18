# Mkhanyisi Gamedze
# Yesware coding challenge
# December 8 2019
# email: mkhanyisi.g@gmail.com
# phone : 2076169348/ 7865491972

# load packages
import math
import random
import sys
from collections import Counter

if __name__ == "__main__":
	
	if (len(sys.argv)<2):
		print ("processor.py <filename>\n*not enough arguments*")
		sys.exit()
		
	filename= sys.argv[1]
	
	# textfile to write to
	stdoutOrigin=sys.stdout 
	sys.stdout = open("output.txt", "w")
	
	# store fullnames in pandas dataframe
	#df = pd.DataFrame(columns=['Lastname','Firstname'])
	
	
	dictionary=dict()
	fullnames=[]
	fullarr=[]
	lastnames=[]
	firstnames=[]
	fullNset=set()
	lastNset=set()
	firstNset=set()
	
	print("### opening file\n")
	f = open(filename, "r") # open file
	
	#print(f.readline())
	#print(f.readline())
	for curline in f:
		# check if the current line
		# starts with "   " or tab
		if curline.startswith("    "):
			#print("*")
			pass
		else:
			comb=curline.split(" -- ")[0]
			fullname= comb.split(", ")
			#print(fullname)
			fullnames.append(comb)
			fullarr.append(fullname)#store fullname array
			lastnames.append(fullname[0])
			firstnames.append(fullname[1])
			
			fullNset.add(comb.lower())
			firstNset.add(fullname[1].lower())
			lastNset.add(fullname[0].lower())
				

	print("### closing file")
	f.close() # close file
	
	# ****** Processing   *********  #
	
	
	#print ("dataframe :",modDF)
	print ("\n** fullnames:\n",len(fullnames))
	print ("\n** lastnames:\n",len(lastnames))
	print ("\n** firstnames:\n",len(firstnames))
	
	print ("\n ## sets\n")
	print ("\n ** Unique fullnames :",len(fullNset))
	print ("\n ** Unique firstnames :",len(firstNset))
	print ("\n ** Unique lastnames :",len(lastNset))
	
	fullNcounts = Counter(fullnames)
	firstNcounts = Counter(firstnames)
	lastNcounts = Counter(lastnames)
	
	print ("\n ** Most Common Lastnames: ", lastNcounts.most_common(10))
	print ("\n ** Most Common Firstnames: ", firstNcounts.most_common(10))
	
	#   A list of 25 specially unique names
	
	fn=set()
	ln=set()
	names=[]
	modified=set()
	
	# test data
	#fullarr=[["Smith", "Joan"],["Smith","John"],["Smith", "Sam"],["Thomas", "Joan"],["Upton", "Joan"],["Upton", "Tom"],["Vasquez", "Cesar"]]
	
	#random.shuffle(fullarr) # uncomment to shuffle
	
	for lname, fname in fullarr:
		#print (lname,fname)
		l = lname in ln
			
		f = fname in fn
		
		#print (l,f)

		if(l==False and f==False):
			ln.add(lname)
			fn.add(fname)
			
			names.append(lname+" "+fname)
			
			modified.add(lname+" "+fname)
		
		if(len(names)>=25):
			print ("limit : BREAK")
			break
		
	print("sets :\n ** fn\n",fn,'\n ** ln \n',ln,"\n ** modified:\n"," length",len(modified),"\n",modified)
	print ("\n************************\n Unique names:\n","length: ",len(names),"\n",names)
	
	fused = set()
	lused=set()
	full=set()
	modified_names=[]
	
	for lname, fname in fullarr:
		# values in unique sets used earlier
		l = lname in ln
		f = fname in fn
		
		# should not be in words used for modified list
		lu = lname in lused
		fu = fname in fused
		
		m= (lname+" "+fname) in modified
		
		
		if(l==True and f==True and m==False and lu==False and fu ==False):
			
			modified_names.append(lname+' '+fname)
			
			fused.add(fname)
			lused.add(lname)
		if(len(modified_names)>25):
			print ("limit : BREAK")
			break
		
	if(len(modified_names)<25):
		print ("\n ## ** Unique name set does not have enough modified names\n")		
	
	print ("\n************************\n Modified names:\n","length: ",len(modified_names),"\n",modified_names[:25])
	
	
	print ("\n*****************************************************************\n")
	print ("##    Mkhanyisi Gamedze : Yesware Coding Challenge Answers     ##")
	print ("\n*****************************************************************\n")
	
	print ("1.\n The unique count of full names (i.e. duplicates are counted only once)")
	
	print ("\n ** Unique fullnames :",len(fullNset))
	
	print ("2.\n The unique count of last names")
	
	print ("\n ** Unique lastnames :",len(lastNset))
	
	print ("3.\n The unique count of first names")
	
	print ("\n ** Unique firstnames :",len(firstNset))
	
	print ("4.\n The ten most common last names (the names and number of occurrences)")
	
	print ("\n ** 10 Most Common Lastnames: \n", lastNcounts.most_common(10))
	
	print ("5.\n The ten most common first names (the names and number of occurrences)")
	print ("\n ** 10 Most Common Firstnames: \n", firstNcounts.most_common(10))
	
	print ("6.\n A list of 25 specially unique names (see below for details)")
	
	print ("\n**\nUnique names:\n","length: ",len(names),"\n",names)
	
	print ("7.\n A list of 25 modified names (see below for details)")
	
	print ("** PROGRAM SHUFFLED EACH TIME TO ENSURE UNIQUE 25 MODIFIED FULL NAMES, (Unomment line 104)")
	
	print ("\n************************\n Modified names:\n","length: ",len(modified_names),"\n",modified_names)
	
	
	if(len(modified_names)<25):
		print ("\n ## ** Unique name set does not have enough modified names to produce 25 unique modified\n")
		
	
	sys.stdout.close()
	sys.stdout=stdoutOrigin