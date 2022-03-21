# print the sum of digites of numbers
#for that we want to seprate the all digites and add the number

num=int(input("Enter the number = "))
ans=0
num1=num
while num>0:
     dig=num%10
     ans=ans+dig
     num=num//10
print("The sum of given numbers ",num1," = ",ans)
