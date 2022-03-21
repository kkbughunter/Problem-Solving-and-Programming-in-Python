#Q.no:9. A website requires the users to input username and password to register.
#Write a program to check the validity of password input by users.
#Following are the criteria for checking the password:
#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#your program should accept a sequence of comma separated passwords and
#will check them according to the above criteria. Passwords that match the
#criteria are to be printed, each separated by a comma. 

import re
def word():
    password=input("enter the password:")
    return password

password=word()
keys=password.split(",")    
length=len(keys)
accepted_pass=[]
for ele in keys:
    if (length<6) and (length>12):
        continue
    elif not re.search("([a-z])+",ele):
        continue    
    elif not re.search("([A-Z])+", ele):
        continue
    elif not re.search("([0-9])+", ele):
        continue
    elif not re.search("([!@$%^&])+", ele):
        continue
    else:
        accepted_pass.append(ele)