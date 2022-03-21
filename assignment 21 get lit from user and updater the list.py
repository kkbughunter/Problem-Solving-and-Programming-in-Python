#21. Get a sequence of numbers from the user and store them in a list. Update the values in the 
#list by adding a constant value obtained from the user to all the elements in the list.
list1=[]
sum=0
i=0
while i==i:
    times=int(input("How many sequence of numbers you want to give : "))
    sum=sum+times
    for i in range(1,times+1):
        text=int(input(f"Enter the sequence of numbers {i} = "))
        list1.append(text)
    exit1=input("Do you want to Exit [y/n] : ")
    if exit1=="y" or exit1=="Y":
        break
print("Your list is = ",list1)

# Update the values in the list by adding a constant value
constant=int(input("please enter the CONSTANT value to add all elements = "))
for ii in range(0,sum):
    a=list1[ii]
    list1[ii]=list1[ii]+constant
print(f"The update by adding a CONSTANT +{constant} = \n",list1)













