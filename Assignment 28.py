# Write a program that accepts a comma separated sequence of words as input 
#       and prints the words in a comma-separated sequence after sorting them alphabetically. 

def lts(x):                                        
    str=" " 
    return str.join(x)

words=input("enter the words separated by comma:")     

low=words.split(",")                                  

a=list(low)                                            
a.sort()                                            
b=lts(a)
print(b) 
