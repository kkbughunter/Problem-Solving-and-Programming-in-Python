# 22. Get a sequence of numbers from the user and store them in a 
# list. Update the values in the list by adding a constant 
# value obtained from the user to all the elements in the list 
# and store the updated values in a new list. 
list1=[]
list2=[]
list3=[]
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
for ii in range(0,sum):
    a=list1[ii]
    list1[ii]=list1[ii]+10
print("The update by adding a CONSTANT (+10) = \n",list1)


#obtained from the user to all the elements in the list and store the updated values in a new list. 
for take2 in list1:
    useradd=int(input(f"How much you want to add for {take2} + "))
    list3.append(take2+useradd)
print("The update by adding a USER = \n",list3)






