# Subdomain_Discover

Python3 program to verify if an email exists or not

Requirements:

pip3 install dnspython3

------------------------------------------------------------------------------------

Download:
  
git clone https://github.com/killeroo7/Email-Existence-Validator.git

cd Email-Existence-Validator

python3 EmailValidatorAdvanced.py --help

------------------------------------------------------------------------------------
Usage:
Options:

  -h, --help                             [-]show this help message and exit
  
  -e email,      --email=EmailAddress    [-]Specify Email Address Ex: killer@yahoo.com
  
  -w WORDLIST,   --wordlist=WORDLIST     [-]Use a wordlist to bruteForce Multiple Emails

  -t THREADS,   --threads=THREADS        [-]Number of threads [default=2]
  
------------------------------------------------------------------------------------
Examples:
1.  python3 Email_Validator_Advanced.py -e killer@gmail.com
2.  python3 Email_Validator_Advanced.py -w wordlist.txt 
3.  python3 Email_Validator_Advanced.py -w wordlist.txt -t 4

'''
Follow on Twitter --> killer007p
'''
