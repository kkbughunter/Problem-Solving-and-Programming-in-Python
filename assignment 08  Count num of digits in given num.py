# 8.  Count the number of digits in a given number

num=int(input("Enter the number : "))
total=0
for i in range(0,len(str(num))):
    total+=1
print(" the number of digits in a given number = ",total)
