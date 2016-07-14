import sys
import time
import urllib2
from bs4 import BeautifulSoup

site1 = "http://www.juexam.org/newexam/show_result.asp?f1="
site2 = "&f2=E3"
site3 = "1622R"

dept = raw_input("\nEnter the first three letter of your exam roll nummber in small letter:\n(For eg if your exam roll number is ABC123456 then enter abc)\n\n")
dept_ = dept.upper()

size =(int)( raw_input("\nEnter the batch size\n"))

exam_roll = 164000 

file_name = "result_"+str(dept_)+".txt"
file = open(file_name, "w")
file.write("ROLL\tNAME\t\tSGPA\n")
print "\n"
for roll in range(1,size+1) :

        result_site = site1 + str(dept) + str(roll + exam_roll) + site2 + str(dept_) + site3       
        page = urllib2.urlopen(result_site)

        soup = BeautifulSoup(page)

        ar1 = []
        ar2 = []
	
	for i in range(10):				#try threading such that printing "processing" and result scraping run simultaneously
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
                        file.write(str(roll)+"\t"+str(ar2[3][0])+"\t  "+str(gpa[7:])+"\n")
                else:
                        file.write(str(roll)+"\t"+str(ar2[3][0])+"\t  "+"X\n")                
        except IndexError:
                pass

file.close()

print("\n\nCOMPLETED\n")
