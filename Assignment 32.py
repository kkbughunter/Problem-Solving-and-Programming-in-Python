# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. 
#       The numbers obtained should be printed in a comma-separated sequence on a single line.
 
m=int(input("enter the intial value:"))
n=int(input("enter the final value:"))
a=[]

for i in range(m,n+1,1): 
   num=i 
   condition=True  
   while(num!=0):  
       digit=num%10 
       num=num//10    

       if(digit%2!=0): 
           condition=False 
           break 
   if(condition):  
       a.append(i) 
print(a)