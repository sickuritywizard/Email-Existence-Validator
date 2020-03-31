#!/usr/bin/env python3

'''
Follow on Twitter	--> killer007p

'''

import re,smtplib,socket,threading
from dns import resolver

import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('-e','--email',dest="email", help="Email To Verify")
	parser.add_argument('-w','--wordlist',dest="wordlist", help="Wordlist File of email")
	parser.add_argument('-t','--threads',dest="threads", help="Total Number of Threads")
	args=parser.parse_args()

	if not args.wordlist and not args.email:							
		parser.error("Specify Either Email address or Wordlist File")
	elif args.wordlist and args.email:
		parser.error("Specify Either Email Address Or Wordlist File ")		
	else:
		return args

def num_of_lines(wordlist):
    num_lines=0
    with open(wordlist,"r") as fp:
        for line in fp:
            num_lines +=1         					  
        return num_lines



def singleEmailVerification(email):
	print("---------------------------------------------------------------------------\n\t\t\t\tKILLER007\n---------------------------------------------------------------------------\n")
	emailToVerify = email
	matchFound = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailToVerify)	#It returns None if no match

	if matchFound == None:
		print('Invalid Email Format')
		exit(1)

	user,domain = emailToVerify.split('@')

	AllMXrecords = resolver.query(domain,'MX')			
	mxRecord = str(AllMXrecords[0].exchange)			

	host = socket.gethostname()							

	server = smtplib.SMTP()								
	server.set_debuglevel(0)							

	server.connect(mxRecord)					       
	server.helo(host)			    			       
	server.mail('hey@gmail.com')				       
	code,msg = server.rcpt(str(emailToVerify))         
	server.quit()									   

	if code==250:									    
		print(emailToVerify+" Exists")
	else:
		print(emailToVerify+" does not exist")


def wordListVerification(begin,end,wordlist):
	startLine = begin
	endLINE = end
	with open(wordlist, "r") as wordlist_file:	
		for line in range(startLine):					
			wordlist_file.readline()
		for line in wordlist_file:
			emailToVerify = line.strip()				
			print("[+]Trying --> "+emailToVerify)		
			
			matchFound = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailToVerify)
		
			if matchFound == None:
				print('Invalid Email Format')
				exit(1)
		
			user,domain = emailToVerify.split('@')
		
			AllMXrecords = resolver.query(domain,'MX')			
			mxRecord = str(AllMXrecords[0].exchange)			
		
			host = socket.gethostname()							
		
			server = smtplib.SMTP()								
			server.set_debuglevel(0)							
		
			server.connect(mxRecord)					       
			server.helo(host)			    			       
			server.mail('hey@gmail.com')				       
			code,msg = server.rcpt(str(emailToVerify))         
			server.quit()									   
		
			if code==250:									   
				print("\n----------------------------------------------\n[+] Valid Email:  "+emailToVerify+"\n----------------------------------------------\n")
			# else:
				# print("[+] "+emailToVerify+"     Does Not Exist")
		
			startLine += 1
			if startLine == endLINE:  
				break				

args = get_arguments()

if(args.email):
	singleEmailVerification(args.email)

if(args.threads):
	total_threads = int(args.threads)
else:
	total_threads = 2


if(args.wordlist):
	print("----------------------------------------------------\n\t\tKILLER007\n----------------------------------------------------")
	print("Starting Email Validation With "+str(total_threads)+" Threads\n")
	total_words = num_of_lines(args.wordlist)
	each_thread_words = int(total_words / total_threads)
	begin = 0  											
	end = each_thread_words  							

	for i in range(total_threads):  					
		t = threading.Thread(target=wordListVerification, args=(begin,end,args.wordlist))  
		t.start()  										    
		begin += each_thread_words  						
		end += each_thread_words


'''
Follow on Twitter	--> killer007p

'''