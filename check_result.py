import sys, time, urllib2, os
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

# Common part of the url of result
site1 = "http://www.juexam.org/newexam/show_result.asp?f1="
site2 = "&f2=E3"
site3 = "R"

class Result :
	code = ""	#store the first three letter of exam roll
	roll = 0
	result_site = ""
        year = 0
        
        # Function to take input the details
	def get_details(self):
		
		self.code = raw_input("\nEnter the first three letter of your exam roll number in small letter:\n(For eg if your exam roll number is ABC123456 then enter abc)\n\n")
		self.year = (int)(raw_input("\nEnter year of study : \n"))
       
       # Function to check if result has come out                           
	def check_site(self):
	
		# Checking if page opens
		try:
	    		page = urllib2.urlopen(self.result_site)
			soup = BeautifulSoup(page, "lxml")
			if len(soup.body) < 8:
				return False
			else :
				return True
		except: 
    			return False

	# Function to store summarized detail of a department
	def show_result(self):
	
		# Clear screen	
		os.system('cls' if os.name == 'nt' else 'clear')
		
		# Taking input
		yr = (int)(raw_input("\nEnter year of examination: \n"))
		sem = (int)(raw_input("\nEnter 1 for odd semester and 2 for even semester :\n"))
		batch_size = (int)(raw_input("\nEnter your batch size :\n"))
		
		sem_copy = sem
        	
        	# Finding the semester, i,e, 1,2,3,4..8
        	sem = self.year*2 - (2-sem)
        	
        	# Generating the exam roll 
		self.roll = (yr%100)*10000 + sem*1000 +5
        	end_site = (yr%100)*100 + self.year*10 + sem_copy
		
		# Generating the url 
		self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) +str(end_site) + site3
		
		if self.check_site() == True :

			# Storing in a text file
			file_name = "result_summary_"+str(self.code)+ str(self.year)+".txt"
			file = open(file_name, "w")
			file.write("ROLL\tNAME\t\t\t  SGPA\n")
			print "\n"

			self.roll = self.roll-4
			
			# Run a loop for the entire department
			for st in range(batch_size) :

				self.result_site =  site1 + str(self.code) + str(self.roll + st) + site2 + str(self.code.upper())+str(end_site) + site3      		 	       
 		       		# Get webpage source code
 		       		page = urllib2.urlopen(self.result_site)

       				soup = BeautifulSoup(page, "lxml")
				
				# Arrays for storing name and CGPA
        			ar1 = []
	        		ar2 = []
				
				# For displaying message
				for i in range(10):
    					print("PROCESSING" + "." * i)
	    				sys.stdout.write("\033[F") # Cursor up one line
    					time.sleep(0.1)
				# Message ends
				
				# Finding SCGPA in source code of webpage
        			for i in soup.find_all("strong"):
                			ar1.append(i.contents)
				
				# Finding name in source code of webpage
        			for i in soup.find_all(class_="underlineresult"):
              			  	ar2.append(i.contents)
              			
              			# If student exists, store result in file else continue  	
        			try:
                			gpa = ar1[8][0]
                			
                			# If supple is there write 'X'
                			if(len(ar1[8][0]) > 7):
                        			file.write(str(st+1)+"\t"+str(ar2[3][0]).ljust(20)+"\t  "+str(gpa[7:])+"\n")
                			else:
                        			file.write(str(st+1)+"\t"+str(ar2[3][0]).ljust(20)+"\t  "+"X\n")                
        			except IndexError:
                			pass
			# Closing the file
			file.close()

			# Display the file name where result is stored
			print("\n\nCOMPLETED\nResult is stored in the file : "+ file_name+"\n")

		else :
			print "\nRESULT NOT YET OUT OR INVALID DETAILS.\n\n"
		time.sleep(5)

	# Function to show detailed result
	def show_detailed_result(self):
			
			# Taking some input
                        yr = (int)(raw_input("\nEnter year of examination: \n"))
                        sem = (int)(raw_input("\nEnter 1 for odd semester and 2 for even semester :\n"))
                        batch_size = (int)(raw_input("\nEnter your batch size :\n"))
                        
                        sem_copy = sem
                        
                        # Finding the semester, i,e, 1,2,3,4..8
                        sem = self.year*2 - (2-sem)
                	
                	# Generating exam roll 
                	self.roll = (yr%100)*10000 + sem*1000 +5
                       	end_site = (yr%100)*100 + self.year*10 + sem_copy
                        
                        # Generating url
                        self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) +str(end_site) + site3
			
			# If result is out
			if self.check_site() == True :

				# Store in a file
				file_name = "result_detailed_"+str(self.code)+str(self.year)+".txt"
				file = open(file_name, "w")
				print "\n"
				
				self.roll = self.roll-4
				
				# Run a loop for the batch
				for st in range(batch_size) :
			
					self.result_site =  site1 + str(self.code) + str(self.roll + st) + site2 + str(self.code.upper()) +str(end_site)+ site3     		 	       
 		       			
 		       			# Get webpage source code
 		       			page = urllib2.urlopen(self.result_site)

       					soup = BeautifulSoup(page, "lxml")
					
					# Arrays to store name, subject wise grades and SCGPA
        				ar1 = []
	        			ar2 = []
	        			ar3 = []
			
					# Displaying message
					for i in range(10):
    						print("PROCESSING" + "." * i)
	    					sys.stdout.write("\033[F") # Cursor up one line
    						time.sleep(0.1)
					# Message ends
					
					# Finding SCGPA in source code of webpage
	        			for i in soup.find_all("strong"):
        	        			ar1.append(i.contents)
					
					# Finding name in source code of webpage
        				for i in soup.find_all(class_="underlineresult"):
              				  	ar2.append(i.contents)
					
					# Finding subjects and their grades in webpage
              				for i in soup.find_all("td", class_="tabledata"):
             	 				ar3.append(i.contents)	  	
        				
        				# If student exists
        				try:
                				
                				# Storing in file
                 			       	file.write("SL NO : "+ str(st+1) + "\tNAME : " + str(ar2[3][0])+"\n")		
                        			i = 10
                        			
                        			# Subjects and their grades
                        			while len(ar3[i][0]) > 1 :
							sub = ar3[i][0]
							grade = ar3[i+2][0]
                        				file.write(sub + " : " + grade + "\n")
                        				i = i+4
                        			
                        			# If supple write 'X'
                        			if(len(ar1[8][0]) > 7):
                        				file.write(str(ar1[8][0]) + "\n\n")
                        			else:
                        				file.write("SGPA: X")	
                				
					# Else continue
        				except IndexError:
                				pass

				# Closing file
				file.close()
				
				# Display name of file
				print("\n\nCOMPLETED\nResult is stored in the file : "+ file_name+"\n")
			
			# Result not yet out
			else :
				print "\nRESULT NOT YET OUT OR INVALID DETAILS.\n\n"
			time.sleep(2)

	# Function to check single result
	def show_single_result(self):
	
		# Take roll  as input
		self.roll = (int)(raw_input("\nEnter the numerical of your exam roll number :\n(For eg if your exam roll number is ABC123456 then enter 123456)\n\n"))
                
                yr = self.roll/1000
                seme = yr%10
                seme_copy = seme % 2
                if seme_copy == 0 :
                	seme_copy = 2
                yr = yr - seme
                seme = (seme+1)/2
                yr = (yr + seme)*10 + seme_copy 
		
		# Generating the url
		self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) +str(yr) + site3
		
		if self.check_site() :
                        self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) +str(yr)+ site3      		 	       
 		       	# Get the source code of web page
 		       	page = urllib2.urlopen(self.result_site)

       			soup = BeautifulSoup(page, "lxml")
       			
       			# Arrays to store name, subject wise grades and SCGPA
  			ar1 = []
	        	ar2 = []
	        	ar3 = []
		
			# Finding SCGPA in source code of webpage
	        	for i in soup.find_all("strong"):
                                ar1.append(i.contents)
	
			# Finding name in source code of webpage
        		for i in soup.find_all(class_="underlineresult"):
              			ar2.append(i.contents)
			
			# Finding subjects and their grades in source code of webpage
              		for i in soup.find_all("td", class_="tabledata"):
             	 		ar3.append(i.contents)	  	
        		
        		# If student exists
        		try:
                		# Displaying 	
                 		print("ROLL : "+ str(self.roll) + "\tNAME : " + str(ar2[3][0])+"\n")		
                        	i = 10
                        	
                        	# Subjects and their grades
                        	while len(ar3[i][0]) > 1 :
                                        sub = ar3[i][0]
					grade = ar3[i+2][0]
                        		print(sub + " : " + grade + "\n")
                        		i = i+4
                        	# If supple write 'X'
                        	if(len(ar1[8][0]) > 7):
        				print(str(ar1[8][0]) + "\n\n")
        			else:
        				print("SGPA: X")
        		# Else continue		
        		except IndexError:
                		pass
	
		# Result not yet out
		else :
			print "\nRESULT NOT YET OUT OR INVALID DETAILS\n\n"
		time.sleep(5)
