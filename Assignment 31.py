# Write a program which accepts a sequence of comma separated 4-digit binary numbers as its input.
#         Then check whether they are divisible by 5 or not.
#         The numbers that are divisible by 5 are to be printed in a comma separated sequence.

 
binary=input("enter the comma separated binary digits:") 
bdl=binary.split(",") 
value = []
for digits in bdl:
    num = int(digits,2)
    print (num)
    if (num%5==0):
        value.append(digits)

print (",".join(value)) 