# Write a program to compute 1/2 + 2/3 + 3/4 +...+n/n+1 with a given n input by console (n>0).


def cas(n):
    a=1
    b=2
    c=a/b
    for i in range(0,n):
        c=c+((a+1)/(b+1))
    return c
n=int(input("Enter the number N : "))
print('1/2 + 2/3 + 3/4 +...+',n,'/',n,'+1  :  ',cas(n))
