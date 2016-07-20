from check_result import Result
import os, time

def main():	
	print "\n\n\n"
	for i in range(0,25):		
        	os.system('cls' if os.name == 'nt' else 'clear')
        #print "\n\nWELCOME TO JADAVPUR UNIVERSITY - CHECK-RESULT \n\n MADE BY SUSHANT GUPTA\n\n"
        	print (" "*(25-i) + "WELCOME TO JADAVPUR UNIVERSITY - CHECK-RESULT \n\n" +" "*(25-i) +"\tMADE BY SUSHANT GUPTA\n\n")
       		time.sleep(0.1)
        ob = Result()
        ob.get_details()
        run = True
        while run :
		os.system('cls' if os.name == 'nt' else 'clear')
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

if __name__ == "__main__" :
        main()
