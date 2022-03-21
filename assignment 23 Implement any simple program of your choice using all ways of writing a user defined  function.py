# 24 Implement any simple program of your choice using all ways of writing a user defined function


# ---------------Type 1--------------
"""
def function_name1():         # Function definition
    start=int(input("Enter the number =  "))
    for i in range(0,start+1):
        for j in range(0,i):
            print("*",end=" ")
        print()

function_name1()             # function call


"""
# ---------------Type 2--------------

"""def function_name2(start):         # Function definition
    for i in range(start,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()

start=int(input("Enter the number =  "))
function_name2(start)             # function call


"""
# ---------------Type 3--------------


def function_name3(stop):         # Function definition
    a=0
    b=1
    sum=0
    print(a)
    print(b)
    for i in range(1,stop):
        ans=a+b
        a=b
        b=ans
        sum=sum+ans
    return(sum+1)

start=int(input("Enter the number =  "))
print("the sum of given Fibonacci serise is = ",function_name3(start)) # function call


# ---------------Type 4--------------


def function_name3():         # Function definition
    start=int(input("Enter the number =  "))
    a=0
    b=1
    sum=0
    print(a)
    print(b)
    for i in range(1,start):
        ans=a+b
        a=b
        b=ans
        sum=sum+ans
    return(sum+1)

print("the sum of given Fibonacci serise is = ",function_name3()) # function call



