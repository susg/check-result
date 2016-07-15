import sys
import time
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')
site1 = "http://www.juexam.org/newexam/show_result.asp?f1="
site2 = "&f2=E3"
site3 = "1622R"

class Result :
	code = ""
	roll = 0
	result_site = ""

	def get_details(self):
		self.code = raw_input("\nEnter the first three letter of your exam roll number in small letter:\n(For eg if your exam roll number is ABC123456 then enter abc)\n\n")

	def check_site(self):
	
		try:
	    		page = urllib2.urlopen(self.result_site)
			soup = BeautifulSoup(page)
			if len(soup.body) < 8:
				return False
			else :
				return True
		except: 
    			return False

	def show_result(self):
		yr = (int)(raw_input("\nEnter year of examination: \n"))
		sem = (int)(raw_input("\nEnter the semester, i.e 1,2,3 etc :\n"))
		batch_size = (int)(raw_input("\nEnter your batch size :\n"))

		self.roll = (yr%100)*10000 + sem*1000 +1
		self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) + site3

		if self.check_site() == True :

			file_name = "result_summary_"+str(self.code)+".txt"
			file = open(file_name, "w")
			file.write("ROLL\tNAME\t\tSGPA\n")
			print "\n"

			for st in range(batch_size) :

				self.result_site =  site1 + str(self.code) + str(self.roll + st) + site2 + str(self.code.upper()) + site3      		 	       
 		       		page = urllib2.urlopen(self.result_site)

       				soup = BeautifulSoup(page)

        			ar1 = []
	        		ar2 = []
	
				for i in range(10):
    					print("PROCESSING" + "." * i)
	    				sys.stdout.write("\033[F") # Cursor up one line
    					time.sleep(0.1)
	
        			for i in soup.find_all("strong"):
                			ar1.append(i.contents)

        			for i in soup.find_all(class_="underlineresult"):
              			  	ar2.append(i.contents)
        			try:
                			gpa = ar1[8][0]
                			if(len(ar1[8][0]) > 7):
                        			file.write(str(st)+"\t"+str(ar2[3][0])+"\t  "+str(gpa[7:])+"\n")
                			else:
                        			file.write(str(st)+"\t"+str(ar2[3][0])+"\t  "+"X\n")                
        			except IndexError:
                			pass

			file.close()

			print("\n\nCOMPLETED\nResult is stored in the file : "+ file_name+"\n")

		else :
			print "\nRESULT NOT YET OUT OR INVALID DETAILS.\n\n"

	def show_detailed_result(self):
			yr = (int)(raw_input("\nEnter year of examination: \n"))
			sem = (int)(raw_input("\nEnter the semester, i.e 1,2,3 etc :\n"))
			batch_size = (int)(raw_input("\nEnter your batch size :\n"))

			self.roll = (yr%100)*10000 + sem*1000 + 1

			self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) + site3

			if self.check_site() == True :

				file_name = "result_detailed_"+str(self.code)+".txt"
				file = open(file_name, "w")
				print "\n"

				for st in range(batch_size) :
			
					self.result_site =  site1 + str(self.code) + str(self.roll + st) + site2 + str(self.code.upper()) + site3      		 	       
 		       			page = urllib2.urlopen(self.result_site)

       					soup = BeautifulSoup(page)

        				ar1 = []
	        			ar2 = []
	        			ar3 = []
	
					for i in range(10):
    						print("PROCESSING" + "." * i)
	    					sys.stdout.write("\033[F") # Cursor up one line
    						time.sleep(0.1)
	
	        			for i in soup.find_all("strong"):
        	        			ar1.append(i.contents)
	
        				for i in soup.find_all(class_="underlineresult"):
              				  	ar2.append(i.contents)

              				for i in soup.find_all("td", class_="tabledata"):
             	 				ar3.append(i.contents)	  	
        				try:
                			
                 			       	file.write("ROLL : "+ str(st) + "\tNAME : " + str(ar2[3][0])+"\n")		
                        			i = 10
                        			while len(ar3[i][0]) > 1 :
							sub = ar3[i][0]
							grade = ar3[i+2][0]
                        				file.write(sub + " : " + grade + "\n")
                        				i = i+4
                        			file.write(str(ar1[8][0]) + "\n\n")				

        				except IndexError:
                				pass

				file.close()

				print("\n\nCOMPLETED\nResult is stored in the file : "+ file_name+"\n")

			else :
				print "\nRESULT NOT YET OUT OR INVALID DETAILS.\n\n"

	def show_single_result(self):
		self.roll = (int)(raw_input("\nEnter the numerical of your exam roll number :\n(For eg if your exam roll number is ABC123456 then enter 123456)\n\n"))

		self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) + site3

		if self.check_site() :
                        self.result_site =  site1 + str(self.code) + str(self.roll) + site2 + str(self.code.upper()) + site3      		 	       
 		       	page = urllib2.urlopen(self.result_site)

       			soup = BeautifulSoup(page)
  			ar1 = []
	        	ar2 = []
	        	ar3 = []
	
	        	for i in soup.find_all("strong"):
                                ar1.append(i.contents)
	
        		for i in soup.find_all(class_="underlineresult"):
              			ar2.append(i.contents)

              		for i in soup.find_all("td", class_="tabledata"):
             	 		ar3.append(i.contents)	  	
        		try:
                			
                 		print("ROLL : "+ str(self.roll) + "\tNAME : " + str(ar2[3][0])+"\n")		
                        	i = 10
                        	while len(ar3[i][0]) > 1 :
                                        sub = ar3[i][0]
					grade = ar3[i+2][0]
                        		print(sub + " : " + grade + "\n")
                        		i = i+4
                        	print(str(ar1[8][0]) + "\n\n")				

        		except IndexError:
                		pass

		else :
			print "\nRESULT NOT YET OUT OR INVALID DETAILS\n\n"

			
print(chr(27) + "[2J")
print "\n\nWELCOPME TO JADAVPUR UNIVERSITY - CHECK-RESULT \n\n MADE BY SUSHANT GUPTA\n\n"
ob = Result()
ob.get_details()
run = True
while run :
	choice = (int)(raw_input("\nEnter choice: \n1. View your result.\n2. View your batch's detailed result.\n3. View your batch's summarised result.\n4. Change your code\n0.Exit\n"))

	if choice == 1 :
		ob.show_single_result()

	elif choice == 2:
		ob.show_detailed_result()

	elif choice == 3:
		ob.show_result()

	elif choice == 4:
		ob.get_details()
	elif choice == 0:
		run = False

	else:
		print "\nWrong Input\n"
