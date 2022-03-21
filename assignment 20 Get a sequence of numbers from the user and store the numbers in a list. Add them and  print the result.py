# 20. Get a sequence of numbers from the user and store the numbers in a list. Add them and print the result


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
count=0
for i in list1:
    count=count+i
print("The total number of given list is = ",count)





