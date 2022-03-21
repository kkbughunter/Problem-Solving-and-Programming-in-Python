# Write a program which can compute the factorial of a given numbers.
#       The results should be printed in a comma-separated sequence on a single line. 

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

x = int(input("enter the value of x:"))       

for i in range (0,x+1,1):                      
    y=fact(i)
    if i==x:
        print(y,end=".")                       
    else:     
        print(y,end=",")                   
print(" ")
