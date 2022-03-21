# 39. Write a program to compute:
# a. f(n)=f(n-1)+100 when n>0
# b. and f(0)=1
# c. with a given n input by console (n>0).

def times(n):
    if n==0:
        return 0
    else:
        return times(n-1)+100
n=int(input("Enter the number to find f(n)=f(n-1)+100 : "))
if n==0:
    print("f (",n,') = f (',n,"- 1) + 100  =  1 ")
else:
    print("f (",n,') = f (',n,"- 1) + 100  = ",times(n))






