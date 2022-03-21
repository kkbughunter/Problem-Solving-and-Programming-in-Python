#  Write a program that accepts a sequence of whitespace separated words as input 
#        and prints the words after removing all duplicate words and sorting them alphanumerically. 


def lts(x):                                
    str=" " 
    return str.join(x)
    
text= input("Please enter any text:")    
lat=text.lower()                         
words=lat.split()

lwdw=list(set(words)) 
lwdw.sort() 
ltsc=lts(lwdw)
print(ltsc)
