# Write a program that accepts sequence of lines as input and
#       prints the lines after making all characters in the sentence capitalized.

def lts(x):                
    str="" 
    for ele in x:
        str += ele
    return str

line=input("enter the line:")  

a=list(line)                       
b=[]

for i in range (0,len(a),1):
    b += str(a[i]).capitalize()    
c=lts(b)                           

print(c)  
 