#Input: N = 25, D = 2
#Output: 1
#Input: N = 100, D = 0
#Output: 2
#  Print all the occurrences of a number in a given list of numbers

num=int(input("Pleace enter the number = "))
check=int(input("Enter the checking number = "))

nums=str(num)
checks=str(check)
count=0

if checks in nums:
    for i in nums:
        if i==checks:
            count+=1
print("the occurrences of a number in a given list ",count)


#----------------------------------------------------------------------#


print("-----USING LIST-----")

getlist=input("Create the list (separate using , ): ")
list1=getlist.split(",")


count=0
a=0
check=int(input("Enter the checking number = "))
checks=str(check)


for i in list1:
    if checks in i:
        for j in i:
            if j==checks:
                count+=1
                a=1
        print("The occurrences of a number in a given list ",count)

if a==1:
    print( )
else:
    print("The given number is not IN LIST :(")
    






